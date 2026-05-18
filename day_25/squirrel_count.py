import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent
df = pd.read_csv(BASE_PATH / "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_data = df["Primary Fur Color"]
colors = color_data.unique()

color_count = []
for color in colors[1:]:
    color_count.append(int((color_data == color).sum()))

data_dict = {
    "Fur Color": colors[1:],
    "Count": color_count
}

data = pd.DataFrame(data_dict)
data.to_csv(BASE_PATH / "squirrel_count.csv")
