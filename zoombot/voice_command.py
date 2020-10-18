from pytube import YouTube
from pytube.request import stream as pt_stream
from typing import Generator, Any, List

from .bases import VoiceCommand, InputStream


class YoutubeStream(InputStream):
    def __init__(self, url: str):
        self.url = url

    def _start_stream(self) -> Generator[Any, Any, None]:
        # Use lowest resolution for now
        download_url = YouTube(self.url).streams[0].url
        yield from pt_stream(download_url)


class YoutubeVoiceCommand(VoiceCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.query: str = ""

    def _search(self, query) -> List[str]:
        pass

    @property
    def data(self) -> InputStream:
        url = self._search(self.query)[0]
        return YoutubeStream(url)


class SpotifyVoiceCommand(VoiceCommand):
    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass
