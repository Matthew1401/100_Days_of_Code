# Day 7 Project: Hangman

import random
import os
clear = lambda: os.system('cls')
clear()

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(""" 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)

life = 7
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_as_list = ["_"] * len(chosen_word)
word_as_string = " ".join(word_as_list)

print(chosen_word)
print(word_as_string)

while "_" in word_as_list:
  if life <= 6:
    print(stages[life])
    if life == 0:
      break
  guessed_letter = input("Guess the letter: ").lower()
  if not guessed_letter in chosen_word:
    life -= 1
  else:
    for number in range(0, len(chosen_word)):
      if chosen_word[number] == guessed_letter:
        word_as_list[number] = guessed_letter
        word_as_string = " ".join(word_as_list)
  print(word_as_string)

if not "_" in word_as_list:
  print("You win!")
else:
  print("You lose.")