import pandas as pd
# # with open("weather_data.csv") as file:
# #     data = file.readlines()

# # print(data)

# # import csv

# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperature = []
# #     dataa = []
# #     print(data)
# #     for row in data:
# #         if row[1] == 'temp':
# #             pass
# #         else:
# #             temperature.append(int(row[1]))

# # print(temperature)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])

# data_dict = data.to_dict()
# # print(data_dict)

# sum_of_temps = 0
# temp_list = data["temp"].to_list()
# for temp in temp_list:
#     sum_of_temps += temp

# # print(f"Temperature Max For The Previous 7 Days: {data["temp"].max()}") 

# # print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]

# # print(f"Monday's temperature in Fahrenheit is: {(monday.temp * 9/5) + 32}F")

# print(monday.temp)

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260224.csv")

Black_rows, columns = df[df["Primary Fur Color"] == "Black"].shape
Cinnamon_rows, columns = df[df["Primary Fur Color"] == "Cinnamon"].shape
Gray_rows, columns = df[df["Primary Fur Color"] == "Gray"].shape
print(df[df["Primary Fur Color"] == "Black"]["Primary Fur Color"])

table = {
    'Fur Color': ['Black', 'Cinnamon', 'Gray'],
    'Count': [Black_rows, Cinnamon_rows, Gray_rows],
}

data = pd.DataFrame(table)
data.to_csv("new_data.csv")