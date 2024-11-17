import pandas

#Create dataframe from data
squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

red_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
gray_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
black_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_color.shape[0], red_color.shape[0], black_color.shape[0]]
    
}

#convet to pandas
summary_frame = pandas.DataFrame(dict)
summary_frame.to_csv("summary_squirrel_count.csv")