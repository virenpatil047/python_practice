# import csv

# #Working with CSV
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     # for row in data:
#     #     print(row)
#     tempratures = []
#     next(data)
#     for row in data:
#         tempratures.append(row[1])
#     print(tempratures)

import pandas as pd

df = pd.read_csv("weather_data.csv")

# head = df.head(2)
# print(df.describe())
# print()
# print(df.tail())

map_data = df.to_dict()

temp_list = df["temp"].to_list()
print(temp_list)
print(sum(temp_list)/len(temp_list))