# Day1
#variables
# Python is object-oriented and dynamically typed.

# When Python encounters:

# name = "Jerrie"

# it creates/uses a string object containing "Jerrie" and makes the name name refer to that object.

# Conceptually:

# name
#   │
#   ▼
# "Jerrie"
# Python variables are names that refer to objects.

name = "Jerrie" 
user_id = 324354545
xp = 266
average_score = 70.7
is_developer = True 
is_dancer = False 

if average_score >= 75:
    print("passed")
else:
    print("Try again")

# #Datatypes - PYTHON figures out the type from the value. that makes python dynamically typed.
print(type(name))
print(type(user_id))
print(type(is_developer))
print(f"my name is {name} I have a score that is higher than {average_score}")
# the f in the print value indicate format string.

print(f"the sum is {average_score + xp}")
print(f"the sum is {average_score // xp}")
print(name == "Jerrie" and is_dancer)

# Getting input from user
# note: input() always returns string
weight = input("what do you weigh? ")
print(f"Jerrie wieghs {weight}")
print(type(weight))

# summmary
name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Next year you will be {age + 1}.")

# NB: Python often favours concise, expressive constructs.