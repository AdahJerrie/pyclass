import random

secret_number = random.randint(1, 100)

print("I am thinking of a number between 1 and 100.") 

while True:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low!")
        print("Try again")
    elif guess > secret_number:
        print("Too high!")
        print("Try again")
    else:
        print("correct!💯")
        break