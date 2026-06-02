# AtomBrain.py

from AtomEyes import Eyes
from AtomMouth import Mouth

from AudioInput import Microphone
from AudioOutput import Speaker

from OpenAIClient import AtomAI


class AtomBrain:

    def __init__(self):

        print("Starting Atom...")

        self.eyes = Eyes()
        self.mouth = Mouth()

        self.mic = Microphone()
        self.speaker = Speaker()

        self.ai = AtomAI()

        self.running = True

    def startup(self):

        self.eyes.center()

        self.mouth.neutral()

        self.eyes.blink_twice()

        print("Atom Ready")

    def process_command(self, text):

        text = text.lower().strip()

        if text == "wink":

            self.eyes.wink_left()

            return None

        if text == "blink twice":

            self.eyes.blink_twice()

            return None

        if text in ["quit", "exit", "shutdown"]:

            self.running = False

            return None

        return self.ai.ask(text)

        def speak_reply(self, reply):
        print(f"Atom: {reply}")

        mp3_file = self.ai.text_to_speech(
            reply,
            "reply.mp3"
        )

        self.mouth.talking()
        self.speaker.speak(mp3_file)

        self.mouth.happy()
        sleep(0.5)
        self.mouth.clear()

    def run(self):

        self.startup()

        while self.running:

            try:

                self.eyes.random_look()

                self.mouth.thinking()

                audio_file = self.mic.record()

                self.eyes.thinking_animation()

                user_text = self.ai.speech_to_text(
                    audio_file
                )

                print(
                    f"You said: {user_text}"
                )

                reply = self.process_command(
                    user_text
                )

                if reply:

                    self.speak_reply(reply)

            except KeyboardInterrupt:

                break

            except Exception as e:

                print(
                    f"Error: {e}"
                )

        self.shutdown()

    def shutdown(self):

        print("Shutting down Atom...")

        self.eyes.center()

        self.mouth.clear()

        self.mic.close()

        self.speaker.close()


if __name__ == "__main__":

    atom = AtomBrain()

    atom.run()
