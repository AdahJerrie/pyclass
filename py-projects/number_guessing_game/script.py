secret_number = 7

while True:
    guess = int(input("Guess the number: "))
    if guess < secret_number:
        print("Too low! Try again")
    elif guess > secret_number:
        print("Too high! Try again")
    else:
        print("Correct!💯")
        break