import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cin_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_squirrels, cin_squirrels, gray_squirrels]
}
df = pandas.DataFrame(data_dict)
df.to_csv("Primary_fur_count.csv")
