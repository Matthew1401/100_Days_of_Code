from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_stuff = CoffeeMaker()
menu = Menu()
money_stuff = MoneyMachine()

coffee = ''
while True:
    coffee = input(f"What would you like? ({menu.get_items()}): ").lower()
    if coffee == 'off':
        break
    if coffee == 'report':
        coffee_stuff.report()
        money_stuff.report()
        continue

    coffee = menu.find_drink(coffee)
    if coffee is None:
        continue

    is_resources = coffee_stuff.is_resource_sufficient(coffee)
    if not is_resources:
        continue

    print(f"The cost is ${coffee.cost}")
    is_paid = money_stuff.make_payment(coffee.cost)
    if not is_paid:
        continue

    coffee_stuff.make_coffee(coffee)
