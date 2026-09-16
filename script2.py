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