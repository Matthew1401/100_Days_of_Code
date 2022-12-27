# Day 8 Project: Ceasar Cipher

import os
clear = lambda: os.system('cls')
clear()


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(text, shift, direction):
    end_text = ""
    if direction == 'decode':
        shift *= -1
    for letter in text:
        if letter == ' ':
            end_text += ' '
        else:
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
    print(f"Your {direction}d message is: {end_text}")

ceasar(text, shift, direction)
