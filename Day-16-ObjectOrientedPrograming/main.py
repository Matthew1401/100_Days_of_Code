from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = ''
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino' or choice == 'report' or choice == 'off':
        break


