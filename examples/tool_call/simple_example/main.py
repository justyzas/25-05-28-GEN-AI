import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
from dispatcher import execute
import json
load_dotenv()

# GEN AI Params
API_KEY = os.getenv("GH_API_TOKEN")
PLATFORM_ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-4.1-mini"
# Other Params
EXIT_KEYWORDS = ["exit", "end", "finish", "bye", "stop", "byebye"]


client = OpenAI(base_url=PLATFORM_ENDPOINT, api_key=API_KEY)
messages = [{"role": "system", "content": "If you get prompted for math, please use the provided tools.\nIf you get prompted with math, please give the answer in this format \"The answer to question {question}, is: \"\""}]

# functions definition:
functions_def = [
    {
        "type": "function",
        "function": {
            "name": "sum",
            "description": "Adds two numbers together",
            "parameters":{
                "type": "object",
                "properties": {
                    "a": { "type" : "number", "description": "The first number"},
                    "b": { "type" : "number", "description": "The second number"}
                },
                "required": ["a", "b"] 
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "uppercase",
            "description": "Makes a text to uppercase",
            "parameters":{
                "type": "object",
                "properties": {
                    "text": { "type" : "string", "description": "The text to be uppercased"},
                },
                "required": ["text"] 
            }
        }
    }
]

while True:
    prompt = input("User: ").strip() # .strip() panaikina tekste pradžioje ir pabaigoje tarpus arba nematomus simbolius
    if prompt.lower() in EXIT_KEYWORDS:
        break # ciklo sustabdymas

    messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        tools=functions_def,
        tool_choice="auto"
    )

    tool_calls = response.choices[0].message.tool_calls
    if tool_calls != None and len(tool_calls) != 0:
        # Tools execution
        for tool_call in tool_calls:
            args = json.loads(tool_call.function.arguments)
            result = execute(tool_call.function.name, **args)
            # Kai AI atsako su užklausa: Iškviesk įrankį (jis jau būna sugalvojęs iššaukimo id), mes tą įrankio iššaukimo faktą turime pridėti kaip vieną iš žinučių AI'ui
            messages.append({"role": "assistant", "tool_calls": [tool_call]})
            # Kai įrankis finale būna iškviečiamas ir gaunamas rezultatas, turime pridėti tokią žinutę AI'ui
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": str(result)})

        # Second call since tools finished their job
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            tools=functions_def,
            tool_choice="auto"
        )
    response_message = response.choices[0].message.content

    print(f"[green]AI: {response_message}[/green]")
    

    


