# -*- coding: utf-8 -*-
# Day 3 Project: Love Calculator

import os
clear = lambda: os.system("cls")
clear()
total1 = 0
total2 = 0

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()


total1 += name1.count("t") + name2.count("t")
total1 += name1.count("r") + name2.count("r")
total1 += name1.count("u") + name2.count("u")
total1 += name1.count("e") + name2.count("e")

total2 += name1.count("l") + name2.count("l")
total2 += name1.count("o") + name2.count("o")
total2 += name1.count("v") + name2.count("v")
total2 += name1.count("e") + name2.count("e")


total = str(total1) + str(total2)
total_as_int = int(total)

if 10 > total_as_int or 90 < total_as_int:
    print(f"Your score is {total_as_int}, you go together like coke and mentos.")
elif 40 < total_as_int > 50:
    print(f"Your score is {total_as_int}, you are alright together.")
else:
    print(f"Your score is {total_as_int}")