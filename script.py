# Engineering logic before language
# To "engineer" logic means to plan it carefully, just as an engineer plans a bridge before pouring concrete.

# Before you write any code, you should be able to answer these questions:

# What is the goal?
# What are the inputs?
# What are the outputs?
# What are the main steps?
# What decisions must be made?
# What can go wrong?
# What should happen when something goes wrong?

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

# NB: Before worrying about syntax, learn to think:
# What should the program DO?
#         ↓
# What decisions does it need to make?
#         ↓
# What data does it need?
#         ↓
# How do I express that in Python?

# THE CONDITIONAL STATEMENT
# if condition: This determines whether the code block will run or not. If the condition is True, the code block runs. If it is False, the code block does not run.
# else: This is optional. It runs a code block if the condition is False.
# elif: This is also optional. It allows you to check multiple conditions. If the first condition is False, it checks the next one, and so on.

# NESTED CONDITIONALS
# Nested if: This is when you have an if statement inside another if statement. It allows you to check multiple conditions in a more complex way.

# 7. Truthiness
# Python allows us to use values directly as conditions.
name = "Jerrie"

if name:
    print("Name was provided.")
# The for loop
for r in range(6):
    print("Jerrie")

# for python you can give a start and stop range.
for r in range(2,6):
    print(r)

# you can also determine the step, that is what happens per loop.

for r in range(2, 10, 3):
    print(r)

# range(start, stop, step)
name = "Jerrie"
for char in name:
    print(char)

# The while loop

# A while loop keeps running while a condition remains true.

count = 1

while count <= 5:
    print(count)
    count = count + 1

# we have the for loop and the while loop.

# while True: creates an infinite loop that runs forever until you manually force it to stop using a break statement inside the loop.

# PRINT vs RETURN
# The mental model

# print():

# "Show this to the user."

# return:

# "Give this value back to whoever called me."

# That's a distinction you'll use constantly in Python.

# Return also ends the function
def check_number(number):
    if number > 0:
        return "Positive"

    return "Not positive"
