import os
from dotenv import load_dotenv
# LangChain OpenAI client
from langchain_openai import ChatOpenAI
from langchain_core import messages

load_dotenv()
token = os.getenv("GH_API_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"



llm = ChatOpenAI(
    base_url=endpoint,
    api_key=token,
    model=model,
    temperature=0.7
)

message = messages.HumanMessage("What is LangChain?")

llm.temperature = 0.8

response = llm.invoke([message])

print(response.content)