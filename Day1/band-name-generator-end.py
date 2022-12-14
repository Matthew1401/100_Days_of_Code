# -*- coding: utf-8 -*-
# This program connect two differents strings and printing it out

import os
clear = lambda: os.system("cls")
clear()

print("Welcome to the Band Name Generator.\nWhat's the name of the city you gre up in?")
city = input()

print("What's your pet's name?")
pets_name = input()

band = city + " " + pets_name
print("Your band name could be", band)