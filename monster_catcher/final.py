import itertools
import random
import time
import sys

monsters = [
    {
        "name": "Pikachu",
        "points": 100,
        "rate": 0.45
    },
    {
        "name": "Lugia",
        "points": 800,
        "rate": 0.10
    }
]

max_turns = 10
score = 0


def start_battle():
    monster = random.choice(monsters)

    print("A wild " + monster["name"] + " appeared!")

    input("Press enter to capture... ")
    show_spinner()

    if random.random() < monster["rate"]:
        print("Captured!! You got " + str(monster["points"]) + " points!")
        global score
        score += monster["points"]
    else:
        print("Aww.. no luck.")


def show_spinner():
    spinner = itertools.cycle(["-", "/", "|", "\\"])

    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")


# Main game
print("Welcome to Almia!")

for i in range(max_turns):
    print("Turn " + str(i + 1))

    start_battle()

    print("Score: " + str(score) + "\n")

print("Final score: " + str(score))
