import chromadb
import embed as em
# Sukuriamas klientas sąveikai su vektorine db
client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = client.get_or_create_collection(name="driving_rules_from_text-embedding-3-small")


# Gauname įvestį iš naudotojo 
user_query = input("Please ask for some information about driving: ")

# Ši funkcija iškviečia OpenAI text-embedding-3-small
user_query_embedded = em.get_embedding(user_query)

results = collection.query(query_embeddings=[user_query_embedded], n_results=2)

print(results["documents"])
print(results["distances"])
print(results["metadatas"])
