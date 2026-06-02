# AudioInput.py

import wave
import pyaudio
import audioop
import time

from config import *

class Microphone:

    def __init__(self):

        self.audio = pyaudio.PyAudio()

    def record(
        self,
        filename="input.wav",
        threshold=500,
        silence_duration=1.5
    ):

        stream = self.audio.open(
            format=pyaudio.paInt16,
            channels=CHANNELS,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE
        )

        print("Listening...")

        frames = []
        started = False
        silence_start = None

        while True:

            data = stream.read(
                CHUNK_SIZE,
                exception_on_overflow=False
            )

            volume = audioop.rms(data, 2)

            if not started:

                if volume > threshold:
                    started = True
                    frames.append(data)

            else:

                frames.append(data)

                if volume < threshold:

                    if silence_start is None:
                        silence_start = time.time()

                    elif (
                        time.time() - silence_start
                        >= silence_duration
                    ):
                        break

                else:
                    silence_start = None

        stream.stop_stream()
        stream.close()

        with wave.open(filename, "wb") as wf:

            wf.setnchannels(CHANNELS)

            wf.setsampwidth(
                self.audio.get_sample_size(
                    pyaudio.paInt16
                )
            )

            wf.setframerate(SAMPLE_RATE)

            wf.writeframes(
                b"".join(frames)
            )

        return filename

    def close(self):

        self.audio.terminate()
