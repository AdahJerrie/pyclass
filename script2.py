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
