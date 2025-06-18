import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
from dispatcher import execute
# result = sum(4, 4.8) 
# print(result) 

sum_function_definition = {
    "name": "sum",
    "description": "Adds two numbers together",
    "parameters":{
        "type": "object",
        "properties": {
            "a": { "type" : "number", "desciption": "The first number"},
            "b": { "type" : "number", "desciption": "The second number"}
        },
        "required": ["a", "b"] 
    }
}
uppercase_function_definition = {
    "name": "uppercase",
    "description": "Makes a text to uppercase",
    "parameters":{
        "type": "object",
        "properties": {
            "text": { "type" : "string", "desciption": "The text to be uppercased"},
        },
        "required": ["text"] 
    }
}



load_dotenv()
token = os.getenv("GH_API_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"


client = OpenAI(base_url=endpoint, api_key=token)


response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "If you get prompted for math, please use the provided tools.\nIf you get prompted with math, please give the answer in this format \"The answer to question {question}, is: \""}, 
        {"role": "user", "content": "What is 23.5 + 6.5"}
    ],
    temperature=0.7,
    tools=[{"type": "function", "function": sum_function_definition }],
    tool_choice="auto"
)


tool_calls = response.choices[0].message.tool_calls

# Checks if any tools were called
if len(tool_calls) != 0:
    # Picks the first tool from the list
    tool_call = tool_calls[0].function
    # executes the tool function
    result = execute(tool_call)
    # Then prints the result
    print(f"[green]{result}[/green]")

if result != None:
    response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "If you get prompted for math, please use the provided tools.\nIf you get prompted with math, please give the answer in this format \"The answer to question {question}, is: \""}, 
        {"role": "user", "content": "What is 23.5 + 6.5"},
        {"role": "assistant", "content": f" the result is: \"{result}\""}
    ],
    temperature=0.7,
    tools=[{"type": "function", "function": sum_function_definition }],
    tool_choice="auto"
)
print(response)

