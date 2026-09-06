name = input("Enter your name: " )
age = int(input("How old are you? "))
country = input("what country do you reside? ")
years_of_experience = int(input("How many years of experience do you have? "))
language = input("what is your favourite programming language? ")
current_language = input("are you currently learning python? ")

is_learning_python = current_language.lower() == "yes"

print("===============================")
print("DEVELOPER PROFILE")
print("===============================")
print(f"Name: {name}") 
print(f"Age: {age}")
print(f"Country: {country}")
print(f"Programming Experience: {years_of_experience} years")
print(f"Favorite Language: {language}")
print(f"Currently Learning Python: {is_learning_python}")