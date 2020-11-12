Collaborated with [Arjun Srivastava](https://github.com/guitarjun), Sanjana Sathyanarayanan, Abhishek Shah

# zoombot
**zoombot** is a chatbot that can talk to meeting participants on [Zoom](https://zoom.us/) 
in real time via voice (no chat messaging necessary), in addition to supporting voice commands for Spotify/YouTube audio.
It leverages Google Cloud's 
[speech synthesis](https://cloud.google.com/text-to-speech) 
and [speech recognition](https://cloud.google.com/speech-to-text) APIs, along 
with state-of-the-art chatbot [Mitsuku](https://www.pandorabots.com/mitsuku/) 
(5-time winner of the Loebner Prize Turing Test). Written
in pure Python!

Requires Python 3.8.

## Dependencies
* [Google Cloud Speech-To-Text](https://pypi.org/project/google-cloud-speech/)
* [Google Cloud Text-To-Speech](https://pypi.org/project/google-cloud-texttospeech/)
* [PyAudio](https://pypi.org/project/PyAudio/)
