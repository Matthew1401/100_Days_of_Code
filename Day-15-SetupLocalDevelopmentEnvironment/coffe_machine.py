# Day 15 Project: Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


# TODO: 1. Ask user to input a choose.
def ask_user_for_input():
    """Asking user for coffee. (espresso/latte/cappuccino or report - for machine resources status)."""
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'espresso' or choice == 'latte' or choice == 'cappuccino' or choice == 'report' or choice == 'off':
            return choice


# TODO: 2. If the input = report, write down the resources.
def write_resources():
    """Writing down the resources of the machine."""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# TODO: 3. Make a function to check, if the resources will senile and if the insert money is enough to buy a coffee.
def update_resources_and_check_the_money(coffee):
    """Checking if the resources are still senile and
    checking if user insert an enough number of money to buy the coffee."""
    global money
    machine_water = resources["water"]
    machine_milk = resources["milk"]
    machine_coffee = resources["coffee"]

    coffee_water = MENU[coffee]['ingredients']['water']
    coffee_milk = MENU[coffee]['ingredients']['milk']
    coffee_coffee = MENU[coffee]['ingredients']['coffee']
    coffee_cost = MENU[coffee]['cost']

    if machine_water < coffee_water:
        print("Sorry there is not enough water.")
        return False
    if machine_milk < coffee_milk:
        print("Sorry there is not enough milk.")
        return False
    if machine_coffee < coffee_coffee:
        print("Sorry there is not enough coffee.")
        return False

    print(f"The cost is {coffee_cost}")
    print("Insert the coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    user_payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    rest_of_money = round(user_payment - coffee_cost, 2)

    if rest_of_money < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    print(f"Here's your ${rest_of_money} in change.")

    money += coffee_cost

    resources["water"] -= coffee_water
    resources["milk"] -= coffee_milk
    resources["coffee"] -= coffee_coffee
    return True


# TODO: 4. Make a function to start the machine and operate the values from there.
def coffee_machine():
    global money
    while True:
        user_choice = ask_user_for_input()
        if user_choice == 'report':
            write_resources()
            continue
        if user_choice == 'off':
            return

        is_coffee_bough = update_resources_and_check_the_money(user_choice)
        if is_coffee_bough:
            print(f"Here's your {user_choice}☕. Enjoy!")


coffee_machine()