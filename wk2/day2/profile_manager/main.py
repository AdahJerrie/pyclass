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
            print("Developer Profile:")

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
                json.dump(developer, file, indent=4)
        except FileNotFoundError:
            print("Developer file not found.")
            continue

    elif choice == "3":
        try:
            with open("developer.json", "w") as file:
                developer = json.load(file)
                new_project = input("Enter new project: ")
                developer["projects"]["current"] = new_project
                json.dump(developer, file, indent=4)
        except FileNotFoundError:
            print("Developer file not found")
            continue

    elif choice == "4":
        print("Goodbye")
        break
    else:
        if choice > 4:
            print(f"{choice} is not a valid option")
