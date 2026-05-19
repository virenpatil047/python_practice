import turtle
import pandas as pd
from pathlib import Path

screen = turtle.Screen()
screen.title("U.S. States Game")

BASE_PATH = Path(__file__).parent
image = str(BASE_PATH / "blank_states_img.gif")

screen.addshape(image)
turtle.shape(image)

df = pd.read_csv(BASE_PATH / "50_states.csv")
state_map = {}
# states = df["state"].tolist()
# print(tuple(df.loc[df["state"] == "Arizona", ["x", "y"]].iloc[0]))
# print(df.loc[df["state"] == "Arizona", ["x", "y"]].values[0].tolist())

for state in df["state"]:
    state_map[state.lower()] = tuple(df.loc[df["state"] == state, ["x", "y"]].iloc[0])

while len(state_map) > 0:
    ans_state = screen.textinput(title=f"{50 - len(state_map)}/50 States Correct", prompt="What's another state's name ?")
    
    if ans_state is None or ans_state == "":
        break
    
    if ans_state == "exit":
        break
    
    if ans_state not in state_map.keys():
        continue
    
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(state_map[ans_state])
    t.write(ans_state.title())
    state_map.pop(ans_state)

states_missed = pd.DataFrame({"states missed" : state_map.keys()})
states_missed.to_csv(BASE_PATH / "states_missed.csv")
