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
