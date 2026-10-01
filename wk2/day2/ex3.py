import json


with open("developer.json", "r") as file:
    developer = json.load(file)

skill = input("Enter your skill: ")

developer["skills"].append(skill)
# print(developer)