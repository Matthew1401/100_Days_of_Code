# Day 5 Project: Average Height

import os
clear = lambda: os.system('cls')
clear()


# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

count = 0
number = 0

for element in student_heights:
    number += element
    count += 1

print(round(number / count))