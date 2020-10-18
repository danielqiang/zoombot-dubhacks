import json
import requests
from pytube import YouTube
from pytube.request import stream as pt_stream
from typing import Generator, Any, List

from .bases import VoiceCommand, InputStream
from .consts import DEFAULT_CHUNK


class YoutubeStream(InputStream):
    def __init__(self, url: str):
        self.url = url

    @staticmethod
    def _mp4_to_wav(mp4_data: bytes) -> bytes:
        from tempfile import NamedTemporaryFile
        from subprocess import call

        mp4 = NamedTemporaryFile(suffix=".mp4")
        wav = NamedTemporaryFile(suffix=".wav")

        try:
            mp4.write(mp4_data)

            command = f"ffmpeg -y -i {mp4.name} {wav.name}"
            call(command, shell=True)

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
        self.query: str = self.message.split('play')[1].split('youtube')[0].strip()
        if self.query.endswith('on'):
            self.query = self.query.split('on')[0].strip()
        elif self.query.endswith('from'):
            self.query = self.query.split('from')[0].strip()

    def _get_video_props(self, video: dict) -> dict:
        video_props = {}

        video_data = video.get("videoRenderer", {})
        video_props["id"] = video_data.get("videoId")
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

    def _search(self, query) -> List[str]:
        while html := requests.get(
            "https://youtube.com/results", params={"search_query": query}
        ).text:
            if 'window["ytInitialData"]' in html:
                video_results = self._parse(html)
                urls = [
                    f'https://www.youtube.com/watch?v={result["id"]}'
                    for result in video_results
                ]
                return urls

    @property
    def data(self) -> Generator[Any, Any, None]:
        url = self._search(self.query)[0]
        return YoutubeStream(url).stream


class SpotifyVoiceCommand(VoiceCommand):
    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass
