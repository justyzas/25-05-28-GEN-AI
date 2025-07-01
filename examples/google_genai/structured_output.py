from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from rich import print


class Ingredient(BaseModel):
    name: str
    amount: float
    measurement_unit: str


class Recipe(BaseModel):
    recipe_name: str
    description: str
    ingredients: list[Ingredient]


load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)

response = client.models.generate_content(
    model=MODEL,
    contents="List a few popular cookie recipes, and include the amounts of ingredients.",
    config={
        "response_mime_type": "application/json",
        "response_schema": list[Recipe],
    }
)

# Visas atsakymas (objektas)
print(response)

# Atsakymo tekstas
print(response.text)

# Pagal paduotą schemą sugeneruotas JSON atsakas
my_recipes: list[Recipe] = response.parsed

# Pirmojo recepto pavadinimas
print(my_recipes[0].ingredients)
