import json

# ----------------------------------------
# 📥 1. JSON String ➡️ Python Object (dict)
# ----------------------------------------

json_string = '{"name": "Alice", "age": 30, "city": "Vilnius"}'
print("🔤 Original JSON string:", json_string)

# Convert JSON string to Python dict
person = json.loads(json_string)
print("📦 Converted to Python object:", person)
print("Name from object:", person["name"])

# ----------------------------------------
# 📤 2. Python Object (dict) ➡️ JSON String
# ----------------------------------------

person_dict = {
    "name": "Bob",
    "age": 25,
    "languages": ["English", "Lithuanian"]
}

# Convert Python dict to JSON string
json_result = json.dumps(person_dict)
print("🔁 Converted to JSON string:", json_result)

# ----------------------------------------
# 🧼 3. Pretty JSON Output (indentation)
# ----------------------------------------

pretty_json = json.dumps(person_dict, indent=4)
print("🖋️ Pretty JSON:\n", pretty_json)

# ----------------------------------------
# 📁 4. Save to and Load from JSON File
# ----------------------------------------

# Save JSON to file
with open("./output/person.json", "w") as f:
    json.dump(person_dict, f, indent=4)
print("💾 Saved to person.json")

# Load JSON from file
with open("./output/person.json", "r") as f:
    loaded_person = json.load(f)
print("📂 Loaded from file:", loaded_person)
