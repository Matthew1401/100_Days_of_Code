# Day 5 Project: Password Generator Project

import os
clear = lambda: os.system('cls')
clear()

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
count_letters = 0
count_symbols = 0
count_numbers = 0

random_number = 0
password = ""


while True:
    if count_letters == nr_letters and count_numbers == nr_numbers and count_symbols == nr_symbols:
        break
    random_number = random.randint(1, 4) # 1 - 3
    if random_number == 1 and count_letters != nr_letters:
        count_letters += 1
        password += random.choice(letters)
        continue
    if random_number == 2 and count_numbers != nr_numbers:
        count_numbers += 1
        password += random.choice(numbers)
        continue
    if random_number == 3 and count_symbols != nr_symbols:
        count_symbols += 1
        password += random.choice(symbols)
        continue
print(f"You password is {password}")

# *Yr(49Tr
# 0)+7YNTR
# M$03(8Xi4c#FO%W
# It works!!