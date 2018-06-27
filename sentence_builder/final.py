import random

names = [ "Bob", "Sheryl", "Jeremy" ]
gross_foods = [ "toenails", "boogers", "earwax" ]

name = random.choice(names)
gross_food = random.choice(gross_foods)

print(name + " likes to eat " + gross_food)
