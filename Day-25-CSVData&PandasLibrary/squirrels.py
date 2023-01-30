import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_Squirrel_Data.csv")
squirrel_black = (data[data["Primary Fur Color"] == "Black"])
squirrel_gray = (data[data["Primary Fur Color"] == "Gray"])
squirrel_red = (data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(squirrel_gray), len(squirrel_red), len(squirrel_black)]
}

squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count.csv")



