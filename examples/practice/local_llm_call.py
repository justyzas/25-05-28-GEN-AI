import requests

response = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "gemma3:1b",
        "messages": [
            {"role": "system", "content": "You are an old grandpa explaining things to the child"},
            {"role": "system", "content": "Start with the sentence 'Back in the days...'"},
            {"role": "user", "content": "What is a chicken?"}
        ],
        "stream": False
    }
)

# print(response.json())
print(response.json()['symbol'])