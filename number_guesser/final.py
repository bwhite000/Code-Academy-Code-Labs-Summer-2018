import random

target = random.randint(1, 100)

while True:
    guess = input("Guess a number: ")

    if guess == target:
        print("Good job!! You got it!")
        break
    elif guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
