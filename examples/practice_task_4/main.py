from fastapi import FastAPI, HTTPException
from models import IngestionBodyModel
from rich import print
from topic_categorization import classify
from vector_store import embed_and_store
app = FastAPI()


@app.get("/test")
def test_connection():
    return "Connection to server was successful"

# POST /ingest


@app.post("/ingest")
def ingest_data_to_llm(body: IngestionBodyModel, chunk_size: int = 500, overlap: int = 100):
    print(body)
    # Klasifikavimas pagal temą
    category = classify(body.text)

    embed_and_store(body, chunk_size=chunk_size,
                    overlap=overlap, topic=category)
    return {"message": f"Successfully teached a model about {category}"}
