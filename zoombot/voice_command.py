from .bases import VoiceCommand, InputStream


class YoutubeVoiceCommand(VoiceCommand):
    @staticmethod
    def is_valid(message: str) -> bool:
        # TODO: Implement
        return False

    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass


class SpotifyVoiceCommand(VoiceCommand):
    @staticmethod
    def is_valid(message: str) -> bool:
        # TODO: Implement
        return False

    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass
