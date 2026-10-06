import json

while True:
    print("=== Developer Profile Manager ===")
    print("1. View profile")
    print("2. Add skill")
    print("3. Change current project")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            with open("developer.json", "r") as file:
                developer = json.load(file)
            print(developer["name"])
            print("age:", developer["age"])
            print("language:", developer["language"])
            print("Skills:")
            for skill in developer["skills"]:
                print(f"  - {skill}")
            print("Current Project:")
            print(f"  - {developer['projects']['current']}")

        except FileNotFoundError:
            print("Developer file not found.")
        except json.JSONDecodeError:
            print("Invalid JSON data.")
            continue

    elif choice == "2":
        try:
            with open("developer.json", "r") as file:
                developer = json.load(file)
                skill = input("Enter a new skill: ")
                developer["skills"].append(skill)
            with open("developer.json", "w") as file:
                json.dump(developer, file, indent=4)
        except FileNotFoundError:
            print("Developer file not found.")
        except json.JSONDecodeError:
            print("Invalid JSON data.")
            continue

    elif choice == "3":
        try:
            with open("developer.json", "r") as file:
                developer = json.load(file)
            new_project = input("Enter new project: ")
            developer["projects"]["current"] = new_project
            with open("developer.json", "w") as file:
                json.dump(developer, file, indent=4)
        except FileNotFoundError:
            print("Developer file not found")
        except json.JSONDecodeError:
            print("Invalid JSON data.")
            continue
    else:
        if choice > "4":
            print(f"{choice} is not a valid option")
