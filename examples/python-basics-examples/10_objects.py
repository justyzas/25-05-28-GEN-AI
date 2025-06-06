# 🧠 Python Objects (Dictionaries) – Real-World Examples and Operations


# JSON - JavaScript Object Notation
# ----------------------------------------
# 🧰 1. Creating an Object (Dictionary)
# ----------------------------------------

person = {
    "name": "Alice",
    "age": 30,
    "city": "Vilnius"
}
print("👤 Person info:", person)

# ----------------------------------------
# ➕ 2. Adding or Updating Items
# ----------------------------------------

person["job"] = "Engineer"  # Add new key-value
print("Added job:", person)

person["age"] = 31  # Update existing key
print("Updated age:", person["age"])

# ----------------------------------------
# ➖ 3. Removing Items
# ----------------------------------------

del person["city"]  # Remove by key
print("Removed 'city':", person)

job = person.pop("job")  # Remove and get value
print(f"Popped job: {job}")
print("After pop:", person)

# ----------------------------------------
# 🔍 4. Accessing Values
# ----------------------------------------

print("Name:", person["name"])

# Safe access (avoids error if key is missing)
print("City:", person.get("city", "Not available"))

# ----------------------------------------
# 🔁 5. Looping Through an Object
# ----------------------------------------

print("🔎 Key-Value Pairs:")
for key, value in person.items():
    print(f"- {key}: {value}")

# ----------------------------------------
# 🔑 6. Get All Keys or Values
# ----------------------------------------

print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# ----------------------------------------
# 🧱 7. Nested Objects
# ----------------------------------------

employee = {
    "name": "Jonas",
    "skills": ["Python", "SQL"],
    "details": {
        "department": "IT",
        "full_time": True
    }
}
print("🏢 Employee info:", employee)
print("Department:", employee["details"]["department"])

# ----------------------------------------
# 📋 8. Object Length
# ----------------------------------------

print("Total fields in 'person':", len(person))

# ----------------------------------------
# 🧬 9. Copying an Object
# ----------------------------------------

person_copy = person.copy()
person_copy["name"] = "Bob"
print("Original:", person)
print("Copied & modified:", person_copy)

# ----------------------------------------
# 🧪 10. Check if Key Exists
# ----------------------------------------

if "name" in person:
    print("✅ 'name' exists in person.")

if "salary" not in person:
    print("❌ 'salary' does not exist.")

# ----------------------------------------
# 🔄 11. Merge Two Objects
# ----------------------------------------

other_info = {"country": "Lithuania", "age": 32}
person.update(other_info)
print("🧩 Merged person:", person)
