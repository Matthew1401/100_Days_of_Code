# Day 4 Project: Banker Roulette
# Important: You are not allowed to use the choice() function.

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

number = random.randint(0, len(names) - 1)
print(f"{names[number]} is going to buy the meal today!")