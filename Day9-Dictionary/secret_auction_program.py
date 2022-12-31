# Day 9: Secrec Aucion Program

import os
clear = lambda: os.system('cls')
clear()

import auction_art
print(auction_art.logo)

auctions = {}
name = ""
bid = 0

def bid():
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    auctions[name] = bid


continue_bidding = ""
while continue_bidding != "no":
    bid()
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear()


max_value = max(auctions.values())
max_key = max(auctions, key=auctions.get)

print(f"The winner is {max_key} with a bid of ${max_value}.")