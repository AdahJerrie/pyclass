# Exercise 1
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Exercise 2: Positive, Negative or zero

number2 = int(input("Enter a number: "))

if number2 > 0:
    print("Number is positive")
elif number2 == 0:
    print("Number is zero")
else:
    print("Number is negative")


# Exercise 3: Multiplication table

number3 = int(input("Enter a number: "))

for i in range(1,11):
    result = number3 * i 
    print(f"{number3} * {i} = {result}")


# while True: creates an infinite loop that runs forever until you manually force it to stop using a break statement inside the loop.