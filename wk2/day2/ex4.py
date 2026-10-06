import json

with open("developer.json", "r") as file:
    developer = json.load(file)
print(developer["projects"]["current"])

new_project = input("Enter your new project: ")

developer["projects"]["current"] = new_project

with open("developer.json", "w") as file:
    json.dump(developer, file, indent=4)

with open("developer.json", "r") as file:
    developer_data = json.load(file)

print(developer_data["projects"]["current"])
