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


# GUI system
game_images = [rock, paper, scissors]
print(game_images[player_choose - 1])

print('Computer chose:')
print(game_images[computer_choose - 1])


# Logical system
if player_choose >= 3 or player_choose < 0:
    print("You typed an invalid number. You lose.")
elif player_choose == 0 and computer_choose == 2:
    print("You win.")
elif computer_choose == 0 and player_choose == 2:
    print("You lose.")
elif player_choose > computer_choose:
    print("You win.")
elif computer_choose > player_choose:
    print("You lose.")
elif player_choose == computer_choose:
    print("It's a draw.") #just for git history XD