from .bases import VoiceCommand, InputStream


class YoutubeVoiceCommand(VoiceCommand):
    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass


class SpotifyVoiceCommand(VoiceCommand):
    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass
