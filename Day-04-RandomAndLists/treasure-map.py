# Day 4 Project: Treasure Map

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

position_x = int(position[0])
position_y = int(position[1])

if 0 < position_x <= 3 and 0 < position_y <= 3:
    map[position_y - 1][position_x - 1] = 'X'
else:
    print('You enter a wrong number. Please enter correct position :)')

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")