from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

import chromadb
from rich import print
from google import genai
from dotenv import load_dotenv
import os
import math

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_API_TOKEN")
MODEL = "gemini-embedding-exp-03-07"

client = genai.Client(api_key=GOOGLE_AI_KEY)


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
    "C:/Users/kruti/Desktop/GEN AI/25-05-28-GEN-AI/examples/RAG/source.txt", encoding="utf-8")

docs = loader.load()

# Sukuriame splitterį, kuris vėliau išdraskys tekstą į gabaliukus
splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,        # Simbolių ilgis
    chunk_overlap=CHUNK_OVERLAP   # Užmetimas ant kito chunk simbolių kiekis
)

# Daliname tekstą gabaliukais
chunks = splitter.split_documents(docs)

# Atgauname sąrašą sudarytą tik iš tekstų
text_contents = [chunk.page_content for chunk in chunks][5:9]
print(f"Got {len(text_contents)} chunks")


# # Atliekame vektorizavimą su tekstų sąrašu
# embeddings = []
# # Mechanizmas, kuris skirtas embedinti po gabaliuką (Kadangi google neleidžia embeddinti daugiau nei 100 tekstų vienu metu).
# for i in range(math.ceil(len(text_contents)/50)):
#     if i + 1 == math.ceil(len(text_contents)/50):
#         current_text_chunks = text_contents[i*50:]
#     else:
#         current_text_chunks = text_contents[i*50:(i+1)*50]
#     response = client.models.embed_content(
#         model=MODEL,
#         contents=current_text_chunks)

#     # Sudarome sąrašą iš embedingų (iš google atgauname objektų sąrašą kuriame yra pats embedding'as)
#     embeddings += [embedding.values for embedding in response.embeddings]

response = client.models.embed_content(
    model=MODEL,
    contents=text_contents)
embeddings = [embedding.values for embedding in response.embeddings]


collection.upsert(
    documents=text_contents,
    ids=[
        f"driving-rule-{rule_number}" for rule_number in range(len(text_contents))],
    embeddings=embeddings,
    # metadatas=[{"source": "KET Lietuva 2025"}]
)
