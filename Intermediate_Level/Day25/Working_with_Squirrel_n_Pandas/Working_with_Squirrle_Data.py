import pandas

data = pandas.read_csv("squirrel_census_data.csv")

gray_data = data[data["Primary Fur Color"] == "Gray"]
black_data = data[data["Primary Fur Color"] == "Black"]
red_data = data[data["Primary Fur Color"] == "Cinnamon"]

gray_count = len(gray_data)
black_count = len(black_data)
red_count = len(red_data)

data_dict = {
    "colors": ["gray", "black", "red"],
    "count": [gray_count, black_count, red_count]
}

pandas.DataFrame(data_dict).to_csv("squirrel_color_count.csv")
