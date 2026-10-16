import csv

# Exercise 4: Appending CSV Records
user_name = input("Enter name: ")
user_skill = input("Enter skill: ")
skill_level = input("Enter skill level: ")

with open("skills.csv", "a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([user_name, user_skill, skill_level])
    
with open ("skills.csv", "r") as file:
    reader = csv.DictReader(file)

    print("=== Developer Skills ===")

    for developer in reader:
        name = developer["name"]
        skill = developer["skill"]
        level = developer["level"]

        print(f"{name}, {skill}, {level}")