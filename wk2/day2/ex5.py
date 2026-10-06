import json
try:
    with open("developer.json", "r") as file:
        developer = json.load(file)
    print(developer["name"])
except FileNotFoundError:
    print("Developer file not found.")
except json.JSONDecodeError:
    print("Invalid JSON data.")