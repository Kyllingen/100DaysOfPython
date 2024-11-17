
import csv
import pandas


temperature = []
# open weather file and read contents into a list
with open("./weather.csv") as weather:
    weather_data = csv.reader(weather)
    

    for row in weather_data:
        if row[1] != "temp":
            temperature.append(int(row[1]))    
print (temperature)

# use pandas this time
data = pandas.read_csv("./weather.csv")
print(data["temp"])

#calculate the average via a list
temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(average)

#calculate through Series mean
print(data["temp"].mean())

#get max value of temps
print(data["temp"].max())

#Get a row in pandas
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

#get temp and convert to fahrenheit
monday = data[data.day == "Monday"]
monday_temp_fahrenheit = monday.temp * 9/5 + 32
print(monday_temp_fahrenheit)


#Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 63]
}
data_dict_frame = pandas.DataFrame(data_dict)
print(data_dict_frame)