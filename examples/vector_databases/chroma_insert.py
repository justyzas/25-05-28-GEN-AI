import chromadb

# Sukuriamas klientas sąveikai su vektorine db
client = chromadb.PersistentClient(path="./vector-db")
# Gaunama kolekcija, kurioje bus saugomi vektoriai ir duomenys
collection = client.get_or_create_collection(name="driving_rules")


# Gauname įvestį iš naudotojo 
information_for_insertion = input("Please enter some information LLM should know: ")
new_rule_number = collection.count() + 1 
# Pridedame į kolekciją "driving_rules" naują įrašą: tai ką parašė naudotojas
collection.add(documents=[information_for_insertion], ids=[f"driving-rule-{new_rule_number}"])

rules_count = new_rule_number

print(f"✅ Successfully added new rule! Now there are {rules_count} rules in total")


