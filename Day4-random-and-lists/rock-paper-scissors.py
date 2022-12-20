# Day 4 Project: Rock Paper Scissors

import random
import os
clear = lambda: os.system('cls')
clear()

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choose = random.randint(0, 2)

if player_choose == 0:
    print(rock)
elif player_choose == 1:
    print(paper)
elif player_choose == 2:
    print(scissors)


print('Computer chose:')
if computer_choose == 0:
    print(rock)
elif computer_choose == 1:
    print(paper)
elif computer_choose == 2:
    print(scissors)


if not 0 <= player_choose <=2:
    print("You have not choose right choice. You lose. ez...")
elif player_choose == 0: # Rock
    if computer_choose == 0: # rock
        print("There is a draw.")
    elif computer_choose == 1: # paper
        print("You lose.")
    elif computer_choose == 2: # scissors
        print("You won!")
elif player_choose == 1: # Paper
    if computer_choose == 0: # rock
        print("You won!")
    elif computer_choose == 1: # paper
        print("There is a draw.")
    elif computer_choose == 2: # scissors
        print("You lose.")
elif player_choose == 2: # Scissors
    if computer_choose == 0: # rock
        print("You lose.")
    elif computer_choose == 1: # paper
        print("You won!")
    elif computer_choose == 2: # scissors
        print("There is a draw.")