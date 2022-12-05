# with open("weather_data.csv", 'r') as weather_file:
#     data = weather_file.readlines()

import csv
with open("weather_data.csv", 'r') as weather_file:
    data = csv.reader(weather_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)


