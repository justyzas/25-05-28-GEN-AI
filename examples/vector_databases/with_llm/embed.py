from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GH_API_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model = "text-embedding-3-small"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Gauname viena embedding is embedding LLM'o
def get_embedding(text: str):
    response = client.embeddings.create(
    input=text,
    model=model,
    )
    return response.data[0].embedding

# Gauname kelis embedding'us is embedding LLM'o
def get_embeddings(texts: list[str]):
    response = client.embeddings.create(
    input=texts,
    model=model,
    )
    embedding_objects_list = response.data
    return [eo.embedding for eo in embedding_objects_list]


# response.data = [
#     embedding1,
#     embedding2,
#     ...
#     embeddingN
# ]

# embeddingX = [1.054616, 0.8765416, .... N]