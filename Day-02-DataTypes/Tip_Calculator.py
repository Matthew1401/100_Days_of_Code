# -*- coding: utf-8 -*-
# Day 2 Project: Tip Calculator

import os
clear = lambda: os.system("cls")
clear()

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


cost_for_person = total_bill / people * (tip / 100 + 1)
print("Each person should pay: $", round(cost_for_person, 2))
