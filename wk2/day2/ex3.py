import json


with open("developer.json", "r") as file:
    developer = json.load(file)

skill = input("Enter your skill: ")

developer["skills"].append(skill)
# print(developer)

with open("developer.json", "w") as file:
    json.dump(developer, file, indent=4)