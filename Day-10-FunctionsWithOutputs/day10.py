# Day 10

# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and conect them into a one string.""" # This is a Docstring, this is a comment to describe what our function is doing
    name = (f"{f_name} {l_name}").title()
    return name

name = format_name("matthew", "kon")
print(name)