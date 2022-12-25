# Day 7 Project: Hangman

import hangman_art
import hangman_words

import random
import os
clear = lambda: os.system('cls')
clear()

stages = hangman_art.stages
print(hangman_art.logo)


life = 7
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_as_list = ["_"] * len(chosen_word)
word_as_string = " ".join(word_as_list)

print(word_as_string)


while "_" in word_as_list:
  if life <= 6:
    print(stages[life])
    if life == 0:
      break
  guessed_letter = input("Guess the letter: ").lower()                                    # Ask player to input a letter
  if not guessed_letter in chosen_word:
    clear()                                                                               # Clear the terminal
    life -= 1
    print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
  else:
    for number in range(0, len(chosen_word)):
      if chosen_word[number] == guessed_letter:
        word_as_list[number] = guessed_letter                                             # Put the guessed letter into a list
        word_as_string = " ".join(word_as_list)                                           # Convert a list into a string
  print(word_as_string)                                                                   # And printed this word as a string

if not "_" in word_as_list:
  print("You win!")
else:
  print("You lose.")