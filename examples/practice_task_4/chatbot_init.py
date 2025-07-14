import os
from openai import OpenAI
from dotenv import load_dotenv


MODEL = "openai/gpt-4.1-mini"


def setup_client():
    TOKEN = os.getenv("OPENAI_API_KEY")
    ENDPOINT = "https://models.github.ai/inference"

    client = OpenAI(
        base_url=ENDPOINT,
        api_key=TOKEN,
    )
    return client


client = setup_client()
print("Chatbot initialized successfully!")
