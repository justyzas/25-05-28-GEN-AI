from google import genai
from dotenv import load_dotenv
import os
from rich import print

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL="gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)

response = client.models.generate_content(
    model=MODEL,
    contents="How does AI work?"
)

#Visas atsakymas (objektas)
print(response)
#Atsakymo tekstas 
print(response.text)