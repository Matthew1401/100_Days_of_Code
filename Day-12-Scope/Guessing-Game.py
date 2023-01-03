# Day 12 Project: Guessing Game

from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def choose_difficulity():
    while True:
        difficulity = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulity == 'easy':
            return EASY_LEVEL_TURNS
        elif difficulity == 'hard':
            return HARD_LEVEL_TURNS

def check_the_answer(player_guess, answer, attempts):
    if player_guess == answer:
        print(f"You got it! The answer was {answer}.")
        return
    elif player_guess > answer:
        print("Too high.")
        return attempts - 1
    elif player_guess < answer:
        print("Too low.")
        return attempts - 1


def game():
    answer = randint(1, 100)

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = choose_difficulity()

    player_guess = 0
    while player_guess != answer:
        print(f"You have {attempts} remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
        attempts = check_the_answer(player_guess, answer, attempts)
        
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return

game()