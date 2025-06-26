from google import genai
from google.genai import types # Tipai, skirti nestandartiniams inputams

from dotenv import load_dotenv
import os
from rich import print

def sum(a:float, b:float):
    "This function will give a sum of a and b numbers"
    print("sum function was just called")
    return a + b

# sum_definition =  {
#         "type": "function",
#         "function": {
#             "name": "sum",
#             "description": "Adds two numbers together",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "a": { "type" : "number", "description": "The first number"},
#                     "b": { "type" : "number", "description": "The second number"}
#                 },
#                 "required": ["a", "b"] 
#             }
#         }
#     }

sum_definition = types.FunctionDeclaration(
    name="sum",
    description="Adds two numbers together",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "a": types.Schema(type=types.Type.NUMBER, description="The first number"),
            "b": types.Schema(type=types.Type.NUMBER, description="The second number")
        },
        required=["a", "b"]
    )
)
print(sum_definition)

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL="gemini-2.5-flash"

client = genai.Client(api_key=GOOGLE_AI_KEY)


tools = types.Tool(function_declarations=[sum_definition])
config = types.GenerateContentConfig(tools=[tools])

response = client.models.generate_content(
    model=MODEL,
    contents="How much is 7.5+8.2?",
    config=config
)

#Visas atsakymas (objektas)
print(response)

function_calls = [resp.function_call for resp in response.candidates[0].content.parts]

#Visų f-jų iššaukimų sąrašas
print(function_calls)

function_call = function_calls[0]

result = sum(function_call.args["a"], function_call.args["b"])

print(f"function call result: {result}")