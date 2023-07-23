import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_amount = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_amount = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_amount = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color": ["gray", "cinnamon", "black"], 
    "Count": [gray_amount, cinnamon_amount, black_amount]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")