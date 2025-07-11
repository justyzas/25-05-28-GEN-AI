import chromadb
from models import IngestionBodyModel
from langchain_text_splitters import RecursiveCharacterTextSplitter
from rich import print

client = chromadb.PersistentClient(path="./vector-db")


def embed_and_store(body: IngestionBodyModel, chunk_size: int, overlap: int, topic: str):
    # Pagal Topic parenkame vector DB kolekcijos pavadinimą
    collection = client.get_or_create_collection(name=topic)
    split_text(text=body.text, chunk_size=chunk_size, overlap=overlap)


def embed(text: str):
    print("text")


def split_text(text: str, chunk_size: int, overlap: int):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap,
        length_function=len,
        is_separator_regex=False,
        # separators=["\t"] # Papildomai galima pasidaryti splitteriui spec simbolių rinkinį, iki kurių jis turėtų splittinti
    )
    texts = text_splitter.create_documents(texts=[text])
    print(texts)
