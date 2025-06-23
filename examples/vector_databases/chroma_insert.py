import chromadb

# Sukuriamas klientas sąveikai su vektorine db
client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = client.get_or_create_collection(name="driving_rules")


# Gauname įvestį iš naudotojo 
information_for_insertion = input("Please enter some information LLM should know: ")
# collection.count() Funkcija, kuri pasako kiek dabar irasu yra kolekcijoje
new_rule_number = collection.count() + 1 
# Pridedame į kolekciją "driving_rules" naują įrašą: tai ką parašė naudotojas
collection.add(documents=[information_for_insertion], ids=[f"driving-rule-{new_rule_number}"])

# Taip pridedame kelis itemus i vektorine duomenu baze:

# collection.add(
#     documents=["document1", "document2", "document3"], 
#     ids=["id1", "id2", "id3"],
#     metadata=[
#         {"source": "teiginiai apie Pythona.txt"},
#         {"source": "anyksciai.txt"},
#         {"source": "teiginiai apie Pythona.txt"},
#     ]
# )

rules_count = new_rule_number

print(f"✅ Successfully added new rule! Now there are {rules_count} rules in total")


