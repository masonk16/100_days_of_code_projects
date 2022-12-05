import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

# print(data["temp"].mean())
max_temp = data["temp"].max()

# Get data in columns
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
fah = (monday.temp * 1.8) + 32
print(fah)

# Create data from scratch
student_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(student_dict)
data.to_csv("students.csv")