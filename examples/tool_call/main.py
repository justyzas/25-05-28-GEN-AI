import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
import json

from tools import get_weather_definition, get_weather
load_dotenv()

# GEN AI Params
API_KEY = os.getenv("GH_API_TOKEN")
PLATFORM_ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-4.1-mini"

# Other Params
EXIT_KEYWORDS = ["exit", "end", "finish", "bye", "stop", "byebye"]


client = OpenAI(base_url=PLATFORM_ENDPOINT, api_key=API_KEY)

messages = [{"role": "system", "content": "You are a helpful assistant. You answer only questions about the weather. You should not expand too much, just focus on the information you get from tools"}]


while True:
    prompt = input("User: ").strip()

    if prompt.lower() in EXIT_KEYWORDS:
        break

    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=[get_weather_definition],
        tool_choice="auto"
    )
    tool_calls = response.choices[0].message.tool_calls

    if tool_calls != None:
        tool_call = tool_calls[0]
        city = json.loads(tool_call.function.arguments)["city"]

        tool_response = get_weather(city)
        tool_response_as_text = json.dumps(tool_response)

        messages.append({"role": "assistant", "tool_calls": [tool_call]})
        messages.append({"role": "tool", "tool_call_id": tool_call.id,
                        "content": str(tool_response_as_text)})

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=[get_weather_definition],
            tool_choice="auto"
        )

    chatbot_response = response.choices[0].message.content

    print(f"[green]AI: [/green] {chatbot_response}")
