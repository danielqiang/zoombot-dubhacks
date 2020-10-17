from .bases import VoiceCommand, InputStream


class YoutubeVoiceCommand(VoiceCommand):
    @staticmethod
    def is_valid(message) -> bool:
        # TODO: Implement
        return True

    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass


class SpotifyVoiceCommand(VoiceCommand):
    @staticmethod
    def is_valid(message) -> bool:
        # TODO: Implement
        return True

    @property
    def data(self) -> InputStream:
        # TODO: Implement
        pass
