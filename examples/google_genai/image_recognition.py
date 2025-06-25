from google import genai
from dotenv import load_dotenv
import os
from rich import print
from google.genai import types

load_dotenv()

with open('resources/auto-lexus.jpg', 'rb') as f:
      image_bytes = f.read()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL="gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)

response = client.models.generate_content(
    model=MODEL,
    contents=["Tell me what's in the following image? Can you be specific on model?", types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg'
      )]
)

#Visas atsakymas (objektas)
print(response)
#Atsakymo tekstas 
print(response.text)