import chromadb

# Sukuriamas klientas sąveikai su vektorine db
client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = client.get_or_create_collection(name="driving_rules")



# Gauname įvestį iš naudotojo 
user_query = input("Please ask for some information about driving: ")

results = collection.query(query_texts=[user_query], n_results=1)
print(results["documents"][0][0])