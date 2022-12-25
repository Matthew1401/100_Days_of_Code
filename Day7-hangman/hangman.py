# Day 7 Project: Hangman

import random
import os
clear = lambda: os.system('cls')
clear()


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guessed_letter = input("Guess the letter: ").lower()

for letter in chosen_word:
    if letter == guessed_letter:
        print("Right")
    else:
        print("Wrong")