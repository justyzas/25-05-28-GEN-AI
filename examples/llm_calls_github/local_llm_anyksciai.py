import requests


model = "jobautomation/OpenEuroLLM-Lithuanian:latest"


with open('./examples/llm_calls_github/anyksciai.txt', 'r', encoding='utf-8') as file:
    context = file.read()

user_prompt = input("Prašome užduoti klausimą apie Anykščius: ")

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an Anyksciai mayor who knows a lot about this town."},
            {"role": "system", "content": "You should answer user questions only about Anyksciai. If user prompts you with some other information, just tell them to ask about Anyksciai."},
            
            {"role": "user", "content": f"context: \"{context}\". question: \"{user_prompt}\""}
        ],
        "stream": False
    }
)

response = response.json()

print(response)