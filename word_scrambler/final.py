import random

words = [ "academy", "summer", "vacation", "pool" ]

word = random.choice(words)
scrambled_word = "".join(random.sample(word, len(word)))

while True:
    print(scrambled_word)
    guess = input("Guess:\n")

    if guess == word:
        print("You win!")
        break
    else:
        print("Try again.\n")
