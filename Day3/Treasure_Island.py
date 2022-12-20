# -*- coding: utf-8 -*-
# Day 3 Project: Treasure Island

import os
clear = lambda: os.system("cls")
clear()


print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************'''
)

print('Welcome to Treasure Island./nYour mission is to find the trasure.')
street = input('You are at a cross the street. Where do you want to go? Type "left or "right"\n').lower()

if street == 'left':
    island = input('You come to a lake. There s an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if island == 'wait':
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
        if door == 'yellow':
            print('Congratulations! You just found a treasure!\nYou Win!')
        elif door == 'red':
            print('You are burned by fire. Idk from where.\nGame Over.')
        elif door == 'blue':
            print('You are eaten by the beast or maybe beasts idk.\nGame Over.')
        else:
            print('Easy, you lose. And you know why.\nGame Over.')
    elif island == 'swim':
        print('You have been atacket by trout.\nGame Over.')
    else:
        print('You just die. Why? Because you did not choose the possible thing.\nGame Over.')
elif street == 'right':
    print('Well, you just fall into a hole.\nGame Over.')
else:
    print('You just die. Why? Because you did not choose the possible thing.\nGame Over.')