# Day 11 Project: Blackjack

import art
import random
import os
clear = lambda: os.system('cls')
clear()


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True
while should_continue:
    play_next = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    clear()
    if play_next == 'n':
        should_continue = False
        break
    
    player_hand = [random.choice(cards), random.choice(cards)]
    current_player_score = sum(player_hand)
    print(f"Your cards: {player_hand}, current score: {current_player_score}")
    
