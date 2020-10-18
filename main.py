from zoombot.streams import SpeechToTextStream, TextToSpeechStream
from zoombot.mitsuku import Mitsuku
from zoombot.consts import Voices, DEFAULT_CHUNK
from zoombot.voice_command import SpotifyVoiceCommand, YoutubeVoiceCommand
from zoombot.schema import VoiceCommandSchema
from zoombot.audio import PlaybackStream

from contextlib import ExitStack
import pyaudio

VOICE = Voices.DEFAULT
USERNAME = "Daniel"
BOTNAME = "ZoomBot"


def _format_message(user: str, message: str):
    from textwrap import fill

    # Remove non-breaking space; assumes `message`
    # only has extended ascii characters
    # (decimal ascii code < 256)
    message = message.replace(chr(160), "")

    # Wrap lines, dropping all whitespace except newlines
    indent = " " * (len(user) + 2)
    lines = []
    for i, line in enumerate(message.split("\n")):
        if i == 0:
            filled = fill(line, subsequent_indent=indent)
        else:
            filled = fill(line, initial_indent=indent, subsequent_indent=indent)
        lines.append(filled)

    formatted = "\n".join(lines)
    return f"{user}: {formatted}"


def talk():
    with ExitStack() as stack:
        stt_stream = stack.enter_context(SpeechToTextStream())
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                language_code=VOICE.language_code,
                voice_name=VOICE.name,
            )
        )
        mitsuku = stack.enter_context(Mitsuku())

        print("ZoomBot initialized. Ready to go!")
        print("=" * 40)

        for message in stt_stream:
            print(_format_message(USERNAME, message))
            response = mitsuku.send(message)
            print(_format_message(BOTNAME, response))
            tts_stream.write(response)


def _sequence_diff(s1: str, s2: str):
    from difflib import SequenceMatcher
    from string import punctuation

    # remove punctuation, casing and leading/trailing whitespace
    trans_table = str.maketrans("", "", punctuation)
    s1 = s1.translate(trans_table).lower().strip()
    s2 = s2.translate(trans_table).lower().strip()

    similarity = SequenceMatcher(a=s1, b=s2).ratio()
    return similarity


def zoom():
    with ExitStack() as stack:
        # vb_cable_input = "CABLE Input (VB-Audio Virtual C"  # speaker
        # vb_cable_output = "CABLE Output (VB-Audio Virtual "  # mic

        stt_stream = stack.enter_context(SpeechToTextStream(punctuation=False))
        tts_stream = stack.enter_context(
            TextToSpeechStream(
                language_code=VOICE.language_code,
                voice_name=VOICE.name,
            )
        )
        mitsuku = stack.enter_context(Mitsuku())

        print("ZoomBot initialized. Ready to go!")
        print("=" * 40)

        prev_response = ""
        for message in stt_stream:
            # ZoomBot currently echos when using VB Cable. If the message
            # is too similar to the previous response, assume it is an echo
            # and skip it.
            # message = 'hey zumba, play happier by marshmello on youtube'

            if _sequence_diff(prev_response, message) > 0.9:
                continue

            print(_format_message(USERNAME, message))
            if VoiceCommandSchema.is_youtube_command(message):
                youtube_vc = YoutubeVoiceCommand(message)

                announcement = f"Now playing: {youtube_vc.video_title}"
                print(_format_message(BOTNAME, announcement))
                tts_stream.write(announcement)
                prev_response = announcement
                data = b"".join(youtube_vc.data)

                playback = PlaybackStream(rate=44100, channels=2)
                for i in range(0, len(data), DEFAULT_CHUNK):
                    chunk = data[i : i + DEFAULT_CHUNK]
                    playback.write(chunk)
                playback.close()
            elif VoiceCommandSchema.is_spotify_command(message):
                spotify_vc = SpotifyVoiceCommand(message)

                announcement = f"Now playing a preview of: {spotify_vc.song} by {spotify_vc.artist}"
                print(_format_message(BOTNAME, announcement))
                prev_response = announcement
                tts_stream.write(announcement)
                data = b"".join(spotify_vc.data)

                playback = PlaybackStream(rate=44100, sample_format=pyaudio.paInt32)
                for i in range(0, len(data), DEFAULT_CHUNK):
                    chunk = data[i : i + DEFAULT_CHUNK]
                    playback.write(chunk)
                playback.close()
            else:
                response = mitsuku.send(message)
                prev_response = response
                print(_format_message(BOTNAME, response))
                tts_stream.write(response)


def main():
    # talk()
    zoom()


if __name__ == "__main__":
    main()
