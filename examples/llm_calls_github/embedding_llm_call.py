import os
from openai import OpenAI
from dotenv import load_dotenv
import numpy as np

texts = [
    "How can I reset my password?",
    "Where can I find my billing history?",
    "How do I contact customer support?",
    "What is the refund policy?",
    "Where can I plant strawberries?"
]

load_dotenv()
token = os.getenv("GH_API_TOKEN")
endpoint = "https://models.inference.ai.azure.com"
model = "text-embedding-3-small"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(text):
    response = client.embeddings.create(
    input=text,
    model=model,
    )
    return response.data[0].embedding

    
initial_embeddings = []

for text in texts:
    embedding = get_embedding(text)
    initial_embeddings.append(embedding)


query = "Where to plant my berries?"

# Get the vector of semantics from AI
question_embedding = get_embedding(query)

similarities = []

for emb in initial_embeddings:
    similarity = cosine_similarity(question_embedding, emb)
    similarities.append(similarity)

best_match_index = np.argmax(similarities)

print(texts[best_match_index])

