import random

max_wrong = 10
amt_wrong = 0

words = [ "moose", "airplane", "computer" ]

word = random.choice(words)
word_length = len(word)

guess_result = []

for i in range(word_length):
    guess_result.append("_")

print(" ".join(guess_result))


def show_guess_progress():
    print(" ".join(guess_result))
    print("")


def is_too_many_wrong():
    return amt_wrong >= max_wrong


def is_done_guessing():
    return "_" not in guess_result

def did_guess_match(guess_val):
    did_match = False

    for i in range(word_length):
        if word[i] == guess_val:
            guess_result[i] = guess_val
            did_match = True

    return did_match


while True:
    guess_val = raw_input("Guess a letter: ")

    if did_guess_match(guess_val) == False:
        amt_wrong += 1
        print("Sorry, wrong guess! Amount wrong: %d/%d" % (amt_wrong, max_wrong))

    if is_too_many_wrong():
        print("Game over! Too many wrong guesses.")
        print("The word was: %s" % word)
        break

    show_guess_progress()

    if is_done_guessing():
        print(word)
        print("Good job - you guessed the word!")
        break
