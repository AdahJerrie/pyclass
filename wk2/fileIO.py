# reading from a file
file = open("note.txt", "r")

content = file.read()

print(content)

file.close()

# now this is shortened with python
with open("note.txt", "r") as file:
    content = file.read()

print(content )

# writing to a file
with open("preview.txt", "w") as file:
    file.write("report received and safely stored")