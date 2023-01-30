# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
print(temp_list)
average_temp = round(sum(temp_list) / len(temp_list), 2)
print(f"Average: {average_temp}")
