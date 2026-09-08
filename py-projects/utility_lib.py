enter_number = int(input("Enter a number: "))

def is_even(number):
    return number % 2 == 0

number_entered = is_even(enter_number)
print(number_entered)

a = int(input("Enter number: "))
b = int(input("Enter number: "))

def get_max(a, b):
    if a > b:
        return a
    else:
        return b
    
max_number = get_max(a, b)
print(max_number)

birth_year = int(input("Enter birth year: "))
current_year = int(input("Enter current year: "))


def calculate_age(birth_year, current_year):
    return current_year - birth_year

age = calculate_age(birth_year, current_year)
print(f"You're {age} years old")