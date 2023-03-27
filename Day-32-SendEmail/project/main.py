import pandas as pd
import random
import datetime as dt


now = dt.datetime.now()
month = now.month
day = now.day

birthday = pd.read_csv("birthdays.csv")
birthday_dict = birthday.to_dict()
print(birthday_dict)

# 2. Check if today matches a birthday in the birthdays.csv
number = 0
for birthday_month in birthday_dict["month"]:
    if birthday_dict["month"][birthday_month] == month:
        if birthday_dict["day"][number] == day:
            print("yolo")
    number += 1

# 3. If step 2 is true, pick a random letter from letter templates
# and replace the [NAME] with the person's actual name from birthdays.csv


