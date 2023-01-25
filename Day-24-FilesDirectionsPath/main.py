with open("../../../my_file.txt") as file:
    contents = file.read()
    print(contents)

# Changing text in our file.
# with open("my_file.txt", mode="w") as file:
#     file.write("New text.")

# Appending text to our file
# with open("my_file.txt", mode="a") as file:
#     file.write("New text.")

# Creating completely new file.
# with open("new_file.txt", mode="w") as file:
#     file.write("New text.")
