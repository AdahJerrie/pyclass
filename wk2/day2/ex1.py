import json

developer = {
    "name": "Jerrie",
    "age": 25,
    "language": "Python",
    "is_learning": True,
    "skills": ["Python", "Go", "FastAPI"]
}

# Convert developer into a JSON string using json.dumps().

jsondev = json.dumps(developer, indent=4)
print(jsondev)

# Convert that JSON string back into a Python object using json.loads().

developers = json.loads(jsondev)
# print(developers)
print(developers["name"])