from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

import chromadb
from rich import print
import os
import requests


CHUNK_SIZE = 850
CHUNK_OVERLAP = 100
# 1. Inicializuoti chromaDB client
# 2. Perskaityti taisykles iš failo source.txt
# 3. Sukapoti tekstą gabaliukais

# 4. Tuos gabaliukus embedinti (gauti vektorius)
# 5. Vektorius talpinti vDB


# Sukuriamas klientas sąveikai su vektorine db
chroma_client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = chroma_client.get_or_create_collection(
    name="driving_rules_from_text-embedding-3-small")

# Užkrauname tekstą iš šaltinio
loader = TextLoader(
    "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/RAG/papildomi_duomenys.txt", encoding="utf-8")

docs = loader.load()

# Sukuriame splitterį, kuris vėliau išdraskys tekstą į gabaliukus
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,        # Simbolių ilgis
    chunk_overlap=CHUNK_OVERLAP   # Užmetimas ant kito chunk simbolių kiekis
)

# Daliname tekstą gabaliukais
chunks = splitter.split_documents(docs)

# Atgauname sąrašą sudarytą tik iš tekstų
text_contents = [chunk.page_content for chunk in chunks]
print(f"Got {len(text_contents)} chunks")

rule_number = 1000
for text in text_contents:
    print(f"Embedding text: {text}")
    response = requests.post("http://localhost:11434/api/embeddings",
                             json={
                                 "model": "nomic-embed-text",
                                 "prompt": text
                             })
    response = response.json()
    embedding = response["embedding"]
    collection.upsert(
        documents=[text],
        ids=[
            f"driving-rule-{rule_number}"],
        embeddings=[embedding],
        # metadatas=[{"source": "KET Lietuva 2025"}]
    )
    rule_number += 1
