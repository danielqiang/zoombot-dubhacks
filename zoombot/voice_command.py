import json
import requests
import spotipy
from pytube import YouTube
from pytube.request import stream as pt_stream
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Generator, Any, List
from pathlib import Path

from .bases import VoiceCommand, InputStream
from .consts import DEFAULT_CHUNK
from . import retry


class YoutubeStream(InputStream):
    def __init__(self, url: str):
        self.url = url

    @staticmethod
    def _mp4_to_wav(mp4_data: bytes) -> bytes:
        from tempfile import NamedTemporaryFile
        from subprocess import call, STDOUT
        from os import devnull

        mp4 = NamedTemporaryFile(suffix=".mp4")
        wav = NamedTemporaryFile(suffix=".wav")

        try:
            mp4.write(mp4_data)

            command = f"ffmpeg -y -i {mp4.name} {wav.name}"
            call(command, shell=True, stdout=open(devnull, "w"), stderr=STDOUT)

            return wav.read()
        finally:
            mp4.close()
            wav.close()

    def _start_stream(self) -> Generator[Any, Any, None]:
        # Use lowest resolution for now
        download_url = YouTube(self.url).streams[0].url
        mp4_data = b"".join(pt_stream(download_url))
        wav_data = self._mp4_to_wav(mp4_data)

        for i in range(0, len(wav_data), DEFAULT_CHUNK):
            chunk = wav_data[i : i + DEFAULT_CHUNK]
            yield chunk


class YoutubeVoiceCommand(VoiceCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.query: str = (
            self.message.split("play", maxsplit=1)[1]
            .rsplit("youtube", maxsplit=1)[0]
            .strip()
        )
        if self.query.endswith("on"):
            self.query = self.query.split("on")[0].strip()
        elif self.query.endswith("from"):
            self.query = self.query.split("from")[0].strip()

        video = self._search(self.query)[0]
        self.video_url = video["url"]
        self.video_title = video["title"]

    def _get_video_props(self, video: dict) -> dict:
        video_props = {}

        video_data = video.get("videoRenderer", {})
        video_props[
            "url"
        ] = f'https://www.youtube.com/watch?v={video_data.get("videoId")}'
        video_props["thumbnails"] = [
            thumb.get("url")
            for thumb in video_data.get("thumbnail", {}).get("thumbnails", [{}])
        ]
        video_props["title"] = (
            video_data.get("title", {}).get("runs", [[{}]])[0].get("text")
        )
        video_props["long_desc"] = (
            video_data.get("descriptionSnippet", {}).get("runs", [{}])[0].get("text")
        )
        video_props["channel"] = (
            video_data.get("longBylineText", {}).get("runs", [[{}]])[0].get("text")
        )
        video_props["duration"] = video_data.get("lengthText", {}).get("simpleText", 0)
        video_props["views"] = video_data.get("viewCountText", {}).get("simpleText", 0)
        video_props["url_suffix"] = (
            video_data.get("navigationEndpoint", {})
            .get("commandMetadata", {})
            .get("webCommandMetadata", {})
            .get("url")
        )
        return video_props

    def _parse(self, html: str):
        # hacky af
        start = (
            html.index('window["ytInitialData"]') + len('window["ytInitialData"]') + 3
        )
        end = html.index("};", start) + 1
        json_str = html[start:end]
        data = json.loads(json_str)

        videos = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
            "sectionListRenderer"
        ]["contents"][0]["itemSectionRenderer"]["contents"]

        results = [
            self._get_video_props(video) for video in videos if "videoRenderer" in video
        ]
        return results

    @retry.on_exception(AssertionError, max_retries=3)
    def _search(self, query) -> List[dict]:
        while html := requests.get(
            "https://youtube.com/results", params={"search_query": query}
        ).text:
            if 'window["ytInitialData"]' in html:
                video_results = self._parse(html)
                assert len(video_results) > 0
                return video_results

    @property
    def data(self) -> Generator[Any, Any, None]:
        return YoutubeStream(self.video_url).stream


class SpotifyStream(InputStream):
    def __init__(self, file):
        self.file = file

    def _start_stream(self) -> Generator[Any, Any, None]:
        try:
            with open(self.file, "rb") as f:
                data = f.read()
                for i in range(0, len(data), DEFAULT_CHUNK):
                    chunk = data[i : i + DEFAULT_CHUNK]
                    yield chunk
        finally:
            Path(self.file).unlink(True)


class SpotifyVoiceCommand(VoiceCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
        song_artist = self.message.split("play")[1].split("by")
        self.song = song_artist[0].strip()
        self.artist = " ".join(song_artist[1].split()[:-2]).strip()
        self._track = None  # Initialized in _spotify_query()
        self._temp_song_file = None  # Initialized in _mp3_to_wav()
        self._byte_data = None  # Initialized in _get_byte_data()

    def _spotify_query(self):
        results = self._spotify.search(
            q="track:" + self.song + " artist:" + self.artist, type="track"
        )
        items = results["tracks"]["items"]
        if len(items) > 0:
            self._track = items[0]

    def _get_byte_data(self) -> bool:
        url = self._track["preview_url"]
        if url is None:
            print(self.song + " has no preview on Spotify!")
            return False
        with requests.Session() as s:
            self._byte_data = s.get(url)
        return True

    def _mp3_to_wav(self):
        from io import BytesIO
        from pydub import AudioSegment

        mp3 = BytesIO(self._byte_data.content)
        sound = AudioSegment.from_mp3(mp3)
        self._temp_song_file = "test.wav"
        sound.export(self._temp_song_file, format="wav")

    @property
    def data(self) -> Generator[Any, Any, None]:
        self._spotify_query()
        self._get_byte_data()
        self._mp3_to_wav()
        return SpotifyStream(self._temp_song_file).stream
