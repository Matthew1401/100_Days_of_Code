# Day 8 Project: Start

# Normal function
def greet():
    print("I")
    print("Love")
    print("U")

greet()


# # Function with one input
def greet_with_name(name=""):
    print(f"Hello {name}")
    print(f"Isn't the weater well {name}?")

greet_with_name("Matthew")


# Function with more than one input
def greet_with_name_and_location(name="", location=""):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with_name_and_location("Matthew", "Warsaw")