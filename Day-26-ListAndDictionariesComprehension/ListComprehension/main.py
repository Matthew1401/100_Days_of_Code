# List Comprehension

# Without comprehension
# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)


# With comprehension
# new_list = [n + 1 for n in numbers]
# print(new_list)


# name = "Matthew"
# new_list = [letter.lower() for letter in name]
# print(new_list)


# new_list = [n for n in range(2, 9, 2)]
# print(new_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)
