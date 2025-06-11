import chromadb
import embed as em
# Sukuriamas klientas sąveikai su vektorine db
client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = client.get_or_create_collection(name="driving_rules_from_text-embedding-3-small")


# Gauname įvestį iš naudotojo 
user_query = input("Please ask for some information about driving: ")

user_query_embedded = em.get_embedding(user_query)

results = collection.query(query_embeddings=[user_query_embedded], n_results=1)

print(results["documents"][0][0])
