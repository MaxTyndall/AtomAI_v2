# OpenAIClient.py

import os
from dotenv import load_dotenv
from openai import OpenAI

from config import CHAT_MODEL, TTS_MODEL, VOICE_NAME

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

class AtomAI:

    def __init__(self):
        self.system_prompt = """
        You are Atom, a friendly robotic assistant.
        Keep answers concise.
        """

    def ask(self, user_message):

        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.choices[0].message.content

    def text_to_speech(self, text, output_file="speech.mp3"):

        with client.audio.speech.with_streaming_response.create(
            model=TTS_MODEL,
            voice=VOICE_NAME,
            input=text
        ) as response:
            response.stream_to_file(output_file)

        return output_file

    def speech_to_text(self, audio_file):

        with open(audio_file, "rb") as f:

            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=f
            )

        return transcript.text
