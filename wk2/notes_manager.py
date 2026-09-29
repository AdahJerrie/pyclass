


print("=== Notes Manager ===")

print("1. Add a note")
print("2. View notes")
print("3. Exit\n")

def notes_manager(optionsss):

    options = input("select an option 1 - 3:\t")
    try:
        selected_option = int(options)
    except ValueError:
        print(f"{options} is not a valid option")
    else:
        while selected_option == 1:
            input_note = input("Enter your note:\t")
            with open("note.txt", "a") as file:
                file.write(f"{input_note}\n")
            break
        while selected_option == 2:
            with open("note.txt", "r") as file:
                for line in file:
                    print(line.strip())
            break
        while selected_option == 3:
            print("Goodbye")
            break


# take_note = input("Add a note:\t")
# with open("note.txt", "a") as file:
#     file.write("=== Notes Manager ===\n")
#     file.write(f"{take_note}\n")

# with open("note.txt", "r") as file:
#     for line in file:
#         print(f"{line}\n")

# print("Goodbye")