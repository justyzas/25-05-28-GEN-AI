from rich import print
from google import genai
from dotenv import load_dotenv
import os
import chromadb
import requests
load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
EMBEDDING_MODEL = "gemini-embedding-exp-03-07"
MODEL = "gemini-2.5-flash"

# Sukuriamas klientas sąveikai su vektorine db
chroma_client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = chroma_client.get_or_create_collection(
    name="driving_rules_from_text-embedding-3-small")

client = genai.Client(api_key=GOOGLE_AI_KEY)

chat = client.chats.create(model=MODEL)

while True:
    prompt = input("Tu: ")

    if prompt == "exit":
        print("Sėkmingai nutraukėte pokalbio sesiją :)")
        break

    response = requests.post("http://localhost:11434/api/embeddings",
                             json={
                                 "model": "nomic-embed-text",
                                 "prompt": prompt
                             })
    response = response.json()
    search_embedding = response["embedding"]

    results = collection.query(
        query_embeddings=[search_embedding], n_results=3)
    # Atgauname pačių tekstų sąrašą
    relevant_texts = results["documents"][0]
    # Tekstus sujungiame, atskirdami naujų eilučių simboliais:
    relevant_texts_joined = "\n".join(relevant_texts)

    response = chat.send_message(
        f"Atsakyk į klausimą naudodamasis pateiktu kontekstu. Jei klausimas nesusijęs su kontekstu, kontekstą ignoruok.\nKontekstas: {relevant_texts_joined}\n Klausimas: {prompt}")

    print(f"AI: {response.text}")
