from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True
while is_on:
    coffee = input(f"What would you like? ({menu.get_items()}): ").lower()
    if coffee == 'off':
        is_on = False
    elif coffee == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        coffee = menu.find_drink(coffee)
        if coffee is not None and coffee_maker.is_resource_sufficient(coffee)\
                and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
