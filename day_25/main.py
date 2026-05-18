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
from pathlib import Path

BASE  = Path(__file__).parent
df = pd.read_csv(f"{BASE}/weather_data.csv")

# Basic methods in CSV
# head = df.head(2)
# print(df.describe())
# print()
# print(df.tail())

# We can map data to different types like map, list ...
# map_data = df.to_dict()

# Average / Mean of Tempratures
# temp_list = df["temp"].to_list()
# print(temp_list)
# print(sum(temp_list)/len(temp_list))

# Alternate way to calculate Mean / Average of Tempratures
# print(df["temp"].mean())

# Maximum value of Tempratures
# print(df["temp"].max())

# Data of Maximum value of Tempratures
# print(df[df["temp"] == df["temp"].max()])

# Monday's temprature in fahrenheit
monday_temp = df[df.day == 'Monday']["temp"][0]
print(f"Monday's temprature : {(monday_temp * 9/5) + 32}")
