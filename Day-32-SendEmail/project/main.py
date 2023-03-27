import pandas as pd
import random
from datetime import datetime


now = datetime.now()
month = now.month
day = now.day

data = pd.read_csv("birthdays.csv")
birthday_dict = data.to_dict()
print(birthday_dict)

# 2. Check if today matches a birthday in the birthdays.csv
number = 0
for birthday_month in birthday_dict["month"]:
    if birthday_dict["month"][birthday_month] == month:
        if birthday_dict["day"][number] == day:
            file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            with open(file_path, mode="r+") as letter:
                content = letter.read()
                content = content.replace("[NAME]", birthday_dict['name'][number])
                print(content)

    number += 1


