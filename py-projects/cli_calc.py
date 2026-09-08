a = int(input("Enter first number: "))
b = int(input("Enter second number: "))




def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return ("Division: Cannot divide by zero.")
    else:
        return a / b
    
add_result = add(a, b)
print(f"Addition: {add_result}")
subtract_result = subtract(a, b)
print(f"Subtraction: {subtract_result}")
multiply_result = multiply(a, b)
print(f"Multiplication: {multiply_result}")
Divide_result = divide(a, b)
print(f"Division: {Divide_result}")

    