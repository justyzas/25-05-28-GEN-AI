import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
from enum import Enum
from rich import print


load_dotenv()
CLASSIFIER_TEXT_LENGTH = 700

TOKEN = os.getenv("OPENAI_API_KEY")
ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-4.1-mini"

client = OpenAI(
    base_url=ENDPOINT,
    api_key=TOKEN,
)

# name containing 3-512 characters from [a-zA-Z0-9._-]


class TopicCategory(str, Enum):
    photography = "Photography"
    driving_rules = "Driving_Rules"
    car_care = "Car_Care"
    house_design_interior = "House_design_and_interior"


class ClassifiedTopic(BaseModel):
    category: TopicCategory


def classify(text: str):
    # client.chat.completions.parse
    response = client.chat.completions.parse(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a classificator chatbot, which classifies long text to a certain topic.",
            },
            {
                "role": "user",
                "content": f"{text[0:CLASSIFIER_TEXT_LENGTH]}...",
            }
        ],
        response_format=ClassifiedTopic
    )

    return response.choices[0].message.parsed.category


classify("55. Važiuoti važiuojamąja dalimi dviračiu leidžiama ne jaunesniems kaip 14 metų asmenims, o išklausiusiems Lietuvos Respublikos švietimo, mokslo ir sporto ministerijos nustatytą")
