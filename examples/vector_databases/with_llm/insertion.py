import chromadb
import embed as em
# Sukuriamas klientas sąveikai su vektorine db
client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = client.get_or_create_collection(name="driving_rules_from_text-embedding-3-small")


# Gauname įvestį iš naudotojo 
prompt = input("Please enter some information LLM should know: ")
new_rule_number = collection.count() + 1
id = new_rule_number

# User input embedding'as
prompt_embedding = em.get_embedding(prompt)

collection.upsert(
    documents=[prompt],
    ids=[f"driving-rule-{new_rule_number}"],
    embeddings=[prompt_embedding],
    metadatas=[{"source": "KET Lietuva 2025", "id": id}]
    )
