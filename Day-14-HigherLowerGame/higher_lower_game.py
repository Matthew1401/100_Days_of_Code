# Day 14 Project: Higher Lower Game

from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')
clear()

a_choose = random.choice(data)
score = 0
is_game_over = False
winner = {}


def get_b_choose():
    while True:
        b_choose_ = random.choice(data)
        if b_choose_ == a_choose:
            continue
        else:
            return b_choose_


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
    else:
        return 0


def format_data(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}."


def game():
    global score, b_choose
    while not is_game_over:
        clear()
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {format_data(a_choose)}")
        print(vs)
        print(f"Against B: {format_data(b_choose)}")

        user_choice = get_input_from_user()
        final_score = score
        score = check_answer(user_choice)
        if score == 0: 
            clear()
            print(f"Sorry, that's wrong. Final score: {final_score}")
            return
        b_choose = get_b_choose()


game()

