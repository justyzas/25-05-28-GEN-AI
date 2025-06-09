import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

# Environment gavimas:
load_dotenv()
token = os.getenv("GH_API_TOKEN")

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

messages = [SystemMessage("You must answer in the shortest way possible. If possible answer with one word")]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def chat(new_message):
    messages.append(UserMessage(new_message))

    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        model=model
    )

    messages.append(AssistantMessage(response.choices[0].message.content))
    print(response)


while True:
    prompt = input("Please enter a question for LLM: ")
    if prompt == "exit":
        print("Thank you for chatting with me. Exiting the conversation...")
        break
    chat(prompt)

print("The end :)")