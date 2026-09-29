import os

while True:
    print("=== Notes Manager ===")

    print("1. Add a note")
    print("2. View notes")
    print("3. Exit\n")
    options = input("select an option 1 - 3:\t\n")
    try:
        selected_option = int(options)
    except ValueError:
        print(f"{options} is not a valid option")
        continue

    if selected_option == 1:
        input_note = input("Enter your note:\t")
        with open("note.txt", "a") as file:
            file.write(f"{input_note}\n")
    
    elif selected_option == 2:
        if not os.path.exists("note.txt"):
            print("No notes found")
        else:
            with open("note.txt", "r") as file:
                for line in file:
                    print(line.strip())
            
    elif selected_option == 3:
        print("Goodbye")
        break
    else:
        if selected_option > 3:
            print(f"{selected_option} is not a valid option")
