# Day 10 Project: Calculator

import os
clear = lambda: os.system('cls')
clear()

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
should_continue = True

while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
        num1 = answer
    else:
        should_continue = False

# should_continue = True
# while should_continue:
#     operation_symbol = input("Pick another operation: ")
#     num3 = int(input("What's the next number?: "))
#     calculation_function = operations[operation_symbol]
#     second_answer = calculation_function(first_answer, num3)
#     print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
#     first_answer = second_answer
#     should_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.: ")

