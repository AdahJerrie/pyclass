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
        return (f"Division: {a / b}")
    
sum = add(a, b)
print("Addition: {sum}")

    