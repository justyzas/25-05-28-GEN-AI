from google import genai
from google.genai import types
import wave
from dotenv import load_dotenv
import os
from rich import print


# Set up the wave file to save the output:
# TTS - Text to speech LLM Models

load_dotenv()


GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-2.5-flash-preview-tts"

client = genai.Client(api_key=GOOGLE_AI_KEY)


def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)


response = client.models.generate_content(
    model=MODEL,
    contents="Say cheerfully in a Scottish accent: Hey, whats up for today?",
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(
            voice_config=types.VoiceConfig(
                prebuilt_voice_config=types.PrebuiltVoiceConfig(
                    voice_name='Kore',
                )
            )
        ),
    )
)

data = response.candidates[0].content.parts[0].inline_data.data

file_name = 'output.wav'
wave_file(file_name, data)  # Saves the file to current directory
