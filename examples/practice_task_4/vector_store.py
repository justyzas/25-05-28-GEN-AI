import chromadb
from models import IngestionBodyModel
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich import print
import requests

client = chromadb.PersistentClient(path="./vector-db")


def embed_and_store(body: IngestionBodyModel, chunk_size: int, overlap: int, topic: str):
    # Pagal Topic parenkame vector DB kolekcijos pavadinimą
    collection = client.get_or_create_collection(name=topic)

    text_chunks = split_text(
        text=body.text, chunk_size=chunk_size, overlap=overlap)

    # 1. - Embeddinti viską ir tik tada dėti į vektorinę duomenų bazę?
    # - Mažiau užklausų į vektorinę duomenų bazę. Sutaupytume tokenų, sutaupomas laikas.
    # - Greitaveika
    # - Duomenų tęstinumas

    # 2. - Embeddinti po vieną chunk, ir jį iš kart dėti į vektorinę duombazę?
    # Jei programa nulūžta, neprarandame visų duomenų (kažkiek jau bus įsirašę į VDB)
    # Lengvesnis kodas
    # Lengvesnis testavimas

    embedded_documents = [{"document": document, "vector": embed(
        document.page_content)} for document in text_chunks]
    # {
    #  "document": #originalus tekstas, metaduomenys
    #  "vector": [0.1654161,0.6654545, 1.2522...]
    # }
    new_rule_number = collection.count() + 1

    documents_to_add = [
        document["document"].page_content for document in embedded_documents]
    ids = [
        f"{topic}-{new_rule_number+i}" for i in range(len(embedded_documents))]

    print(f"Currently added rules to vector database: {new_rule_number - 1}")
    print(documents_to_add)
    print(ids)
    collection.add(
        documents=documents_to_add,
        ids=ids,
        embeddings=[document["vector"] for document in embedded_documents]
    )


def embed(text: str):
    response = requests.post("http://localhost:11434/api/embeddings",
                             json={
                                 "model": "nomic-embed-text",
                                 "prompt": text
                             })
    response = response.json()
    embedding = response["embedding"]
    return embedding


def split_text(text: str, chunk_size: int, overlap: int):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        length_function=len,
        is_separator_regex=True,
        # Papildomai galima pasidaryti splitteriui spec simbolių rinkinį, iki kurių jis turėtų splittinti
        # separators=["[0-9]+\."]
    )
    texts = text_splitter.create_documents(texts=[text])
    return texts
