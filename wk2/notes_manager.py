# === Notes Manager ===

# 1. Add a note
# 2. View notes
# 3. Exit

take_note = input("Add a note:\t")
with open("note.txt", "a") as file:
    file.write("=== Notes Manager ===\n")
    file.write(f"{take_note}\n")

with open("note.txt", "r") as file:
    for line in file:
        print(f"{line}\n")

print("Goodbye")