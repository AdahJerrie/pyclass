def is_numeric(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

    numbers = ["10", "20", "hello", "30", "world", "40"]

    vald_numbers = [int(num) for number in numbers if is_numeric]
    print("valid numbers:", vald_numbers)

    squares = [num**2 for num in vald_numbers]
    print("squares list:", squares)

    unique_squares_set = {num**2 for num in vald_numbers}
    print("unique_square_set:", unique_squares_set)

    squares_dict = {num:num**2 for num in vald_numbers}
    print(squares_dict)

# 1. write a python program to check if a number is even or odd
def is_even(num):
    if num % 2 == 0:
        return num

num_check = eval(input("enter a number\t: "))
if is_even(num_check):
    print(f"{num_check} is even")
else:
    print(f"{num_check} is not even")

# 2. write a python program to check if a number is a multiple of 3, a multiple of 5 or both.
x = eval(input('enter a number      '))
if x % 3 == 0 and x % 5 == 0:
        print(f"this a multiple of 3 and 5: ", x)
elif x % 3 == 0:
    print(f"this is a multiple of 3: ", x)

elif x % 5 == 0:
    print(f"this is a multiple of 5: ", x) 
else:
    print(f"this is not a multiple of 3 or 5: ", x)