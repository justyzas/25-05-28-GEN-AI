from google import genai
from google.genai import types
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

from dotenv import load_dotenv
import os
from rich import print

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)

tools = []
tools.append(Tool(url_context=types.UrlContext))
tools.append(Tool(google_search=types.GoogleSearch))

response = client.models.generate_content(
    model=MODEL,
    contents="ar gali patikrinti Samsung Galaxy S25 Ultra 256GB lietuvoje? Nesigilink į įrenginio parametrus, gauk tik kainas ir tikslias nuorodas į įrenginio prekės puslapį iš kur galima pirkti. Kaip šaltinį naudok https://www.kaina24.lt/p/samsung-galaxy-s25-ultra-256gb/",
    config=GenerateContentConfig(
        tools=tools,
        response_modalities=["TEXT"],
    )
)

# Visas atsakymas (objektas)
print(response)
# Atsakymo tekstas
print(response.text)
