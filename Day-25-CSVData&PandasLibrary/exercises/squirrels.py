import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
squirrel_black = len(data[data["Primary Fur Color"] == "Black"])
squirrel_gray = len(data[data["Primary Fur Color"] == "Gray"])
squirrel_red = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [squirrel_gray, squirrel_red, squirrel_black]
}

squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count.csv")



