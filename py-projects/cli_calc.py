first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))



print(f"Addition: {first_number + second_number}")
print(f"Subtraction: {first_number - second_number}")
print(f"Multiplication: {first_number * second_number}")
# print(f"Division: {first_number / second_number}")


if second_number == 0:
    print("Division: Cannot divide by zero.")
    print("Remainder: Cannot calculate remainder.")
else:
    print(f"Division: {first_number / second_number}")
    print(f"Remainder: {first_number % second_number}")