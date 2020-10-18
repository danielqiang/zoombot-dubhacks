import re


class VoiceCommandSchema:
    @staticmethod
    def is_youtube_command(message: str) -> bool:
        message = message.lower()
        pattern = re.compile("^.* zumba,* play .* (from|on) youtube")
        return bool(pattern.match(message))

    @staticmethod
    def is_spotify_command(message: str) -> bool:
        message = message.lower()
        pattern = re.compile("^.* zumba,* play .* by .* (from|on) spotify")
        return bool(pattern.match(message))
