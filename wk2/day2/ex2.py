import json 

developer = {
    "name": "Jerrie",
    "age": 25,
    "language": "Python",
    "is_learning": True,
    "skills": ["Python", "Go", "FastAPI"]
}

with open("developer.json", "w") as file:
    json.dump(developer, file, indent=4)

with open("developer.json", "r") as file:
    developer_data = json.load(file)

print(developer_data["name"])
print(developer_data["skills"])

# Python object
#      │
#      ├── dumps() ──→ JSON string
#      │
#      └── dump() ───→ JSON file


# JSON string
#      │
#      └── loads() ──→ Python object

# JSON file
#      │
#      └── load() ───→ Python object