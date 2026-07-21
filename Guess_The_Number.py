import random

number = random.randint(1, 100)
guess = 0
attempts = 0

while guess != number:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"Correct! You got it in {attempts} attempts.")
