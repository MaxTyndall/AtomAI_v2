# AudioOutput.py

import os
import wave
import pyaudio
import subprocess


class Speaker:

    def __init__(self):
        self.audio = pyaudio.PyAudio()

    def mp3_to_wav(
        self,
        mp3_file,
        wav_file="speech.wav"
    ):

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                mp3_file,
                "-ac",
                "1",
                "-ar",
                "16000",
                wav_file
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return wav_file

    def play_wav(self, wav_file):

        wf = wave.open(wav_file, "rb")

        stream = self.audio.open(
            format=self.audio.get_format_from_width(
                wf.getsampwidth()
            ),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        chunk = 1024

        data = wf.readframes(chunk)

        while data:

            stream.write(data)

            data = wf.readframes(chunk)

        stream.stop_stream()
        stream.close()
        wf.close()

    def play_mp3(self, mp3_file):

        wav_file = self.mp3_to_wav(mp3_file)

        self.play_wav(wav_file)

        if os.path.exists(wav_file):
            os.remove(wav_file)

    def speak(self, mp3_file):

        self.play_mp3(mp3_file)

    def close(self):

        self.audio.terminate()
