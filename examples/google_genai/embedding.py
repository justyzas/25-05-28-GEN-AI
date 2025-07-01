# Embedding LLM call

from google import genai
from dotenv import load_dotenv
import os
from rich import print

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-embedding-exp-03-07"

client = genai.Client(api_key=GOOGLE_AI_KEY)

response = client.models.embed_content(
    model=MODEL,
    contents=["How does AI work?", "What's the color of the grass?"]
)

# Visas atsakymas (objektas):
print(response)
# Vektorizuotų tekstų sąrašas:
print(response.embeddings)
# Vienas iš vektorizuotų tekstų:
print(response.embeddings[0])
