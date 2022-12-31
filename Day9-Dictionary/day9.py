# Day 9

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Nesting
travel_log = {
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visitis": 14}
}

# Nesting Dictionary in a List
travel_log = [
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg"],
    "total_visitis": 14
    },
    {
    "country": "France",
    "cities_visited": ["Paris", "Dijon"],
    "total_visitis": 7
    },
]

print(travel_log[0]["cities_visited"])