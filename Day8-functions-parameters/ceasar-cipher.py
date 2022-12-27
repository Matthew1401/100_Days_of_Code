# Day 8 Project: Ceasar Cipher

import os
clear = lambda: os.system('cls')
clear()


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(text, shift):
    text_as_list = list(text.strip())
    for i in range(0, len(text_as_list)):
        if text_as_list[i] in alphabet:
            index_number = alphabet.index(text_as_list[i]) + shift
            if index_number > 25:
                index_number -= 26
            text_as_list[i] = alphabet[index_number]
        else:
            continue
    text = "".join(text_as_list)
    print(text)


def decode(text, shift):
    text_as_list = list(text.strip())
    for i in range(0, len(text_as_list)):
        if text_as_list[i] in alphabet:
            index_number = alphabet.index(text_as_list[i]) - shift
        if text_as_list[i] in alphabet:
            text_as_list[i] = alphabet[index_number]
        else:
            continue
    text = "".join(text_as_list)
    print(text)


if direction == 'encode':
    encode(text, shift)
elif direction == 'decode':
    decode(text, shift)
else:
    print("Type 'encode' or 'decode'.\nNothing else ;)")