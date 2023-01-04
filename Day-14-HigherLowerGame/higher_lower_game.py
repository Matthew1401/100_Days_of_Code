# Day 14 Project: Higher Lower Game

from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')
clear()

NUMBER_OF_SEARCH = len(data)
a_choose = data[random.randint(0, NUMBER_OF_SEARCH - 1)]
a_choose_index = data.index(a_choose)
score = 0
is_game_over = False
winner = {}

def get_b_choose():
    while True:
        b_choose_index = random.randint(0, NUMBER_OF_SEARCH - 1)
        if b_choose_index == a_choose_index:
            continue
        else:
            b_choose = data[b_choose_index]
            return b_choose
        
b_choose = get_b_choose()

def get_input_from_user():
    while True:
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if user_choice == 'A': return 'A'
        elif user_choice == 'B': return 'B'

def check_answer(user_choice):
    global a_choose, score
    a_score = a_choose['follower_count']
    b_score = b_choose['follower_count']
    if a_score == b_score: return score + 1
    elif user_choice == 'A' and a_score > b_score:
        a_choose = b_choose
        return score + 1
    elif user_choice == 'B' and a_score < b_score:
        a_choose = b_choose
        return score + 1
    else: return 0


def game():
    global score, b_choose
    while is_game_over == False:
        clear()
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {a_choose['name']}, a {a_choose['description']}, from {a_choose['country']}.")
        print(vs)
        print(f"Against B: {b_choose['name']}, a {b_choose['description']}, from {b_choose['country']}.")

        user_choice = get_input_from_user()
        final_score = score
        score = check_answer(user_choice)
        if score == 0: 
            clear()
            print(f"Sorry, that's wrong. Final score: {final_score}")
            return
        b_choose = get_b_choose()
    
game()

