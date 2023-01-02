# Day 11 Project: Blackjack

from art import logo
import random
import os
clear = lambda: os.system('cls')
clear()

def eleven_into_one(hand=[]):
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return hand

def player_deck(cards):
    """Giving you a two random cards"""
    hand = [random.choice(cards), random.choice(cards)]
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return hand

def computer_deck(cards):
    """Giving you a dealer hand completly"""
    hand = [random.choice(cards), random.choice(cards)]
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    while True:
        if sum(hand) < 17:
            hand.append(random.choice(cards))
            if 11 in hand and sum(hand) > 21:
                hand.remove(11)
                hand.append(1)
        if sum(hand) >= 17:
            break
    return hand

def take_another_card():
    while True:
        should_take_another_card = input("Type 'y' to get another card, typr 'n' to pass: ")
        if should_take_another_card == 'y': return True
        elif should_take_another_card == 'n': return False
        

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True
while should_continue:
    play_next = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    clear()
    if play_next == 'n':
        should_continue = False
        break
    print(logo)

    player_hand = player_deck(cards)
    player_score = sum(player_hand)
    print(f"Your cards: {player_hand}, current score: {player_score}")
    
    computer_hand = computer_deck(cards)
    computer_score = sum(computer_hand)
    print(f"Computer's first card: {computer_hand[0]}")

    while take_another_card():   
        player_hand.append(random.choice(cards))
        player_hand = eleven_into_one(player_hand)
        player_score = sum(player_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")
        if player_score > 21: break
    
    # Checking who is the winner
    clear()
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if player_score > 21:
        print("You went over. You lose.")
    elif computer_score > 21:
        print("The Dealer was shocked out :O")
    elif player_score == computer_score:
        print("It's a draw.")
    elif player_score > computer_score:
        print("You win! Congratulations!")
    else:
        print("You lose.")
