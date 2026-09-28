# reading from a file
# file = open("note.txt", "r")

# content = file.read()

# # print(content)

# file.close()

# now this is shortened with python
with open("note.txt", "r") as file:
    content = file.read()
print("--- My Notes ---")
print(content )

# writing to a file
user_name = input("enter name:\t")
fav_programming_language = input("Enter favourite programming language:\t")
yrs_of_experience = input("enter years of programming experience:\t")

with open("developer.txt", "w") as file:
    file.write("developer profile\n")
    file.write(f"name: {user_name}\n")
    file.write(f"Favorite language: {fav_programming_language}\n")
    file.write(f"Experience: {yrs_of_experience} years\n")

# Appending (a)
new_skill = input("Enter a new skill:\t")
with open("developer.txt", "a") as file:
    file.write(f"new skill: {new_skill}\n")