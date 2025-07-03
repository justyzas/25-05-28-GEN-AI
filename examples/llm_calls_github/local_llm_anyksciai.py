import requests


model = "nomic-embed-text:latest"


# with open('./examples/llm_calls_github/anyksciai.txt', 'r', encoding='utf-8') as file:
#     context = file.read()

# user_prompt = input("Prašome užduoti klausimą apie Anykščius: ")

response = requests.post(
    "http://localhost:11434/api/embeddings",
    json={
        "model": model,
        "prompt": "1. Kelių eismo taisyklės nustato eismo keliais tvarką visoje Lietuvos Respublikos teritorijoje."
    }
)

response = response.json()

print(response["embedding"])
