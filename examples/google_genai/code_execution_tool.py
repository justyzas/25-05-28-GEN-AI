from google import genai
from google.genai import types

from dotenv import load_dotenv
import os
from rich import print


# Set up the wave file to save the output:
# Code execution tool can run python code inside LLM. It can return structured results if needed.
load_dotenv()


GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-2.5-flash-preview-tts"

client = genai.Client(api_key=GOOGLE_AI_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is the sum of the first 10 prime numbers?"
    "Generate and run code for the calculation, and make sure you get all 10.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

print(response)


for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    if part.executable_code is not None:
        print(part.executable_code.code)
    if part.code_execution_result is not None:
        print(part.code_execution_result.output)
