import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GH_API_TOKEN")
print(token)
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def call_llm(user_chatbot_messages):
    messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            }
        ] + user_chatbot_messages
    
    response = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return response

print("Loaded chatbot")
