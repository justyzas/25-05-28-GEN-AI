import chromadb
from rich import print

client = chromadb.PersistentClient(path="./vector-db")
collection = client.get_or_create_collection(name="driving_rules")

# Paprasome visu irasu is chroma duomenu bazes
records = collection.get()


print(records)