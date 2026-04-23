import time
from turtle import Screen, Turtle
from pads import Pads

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arcade Game")
screen.tracer(0)

pads = Pads()

screen.listen()
screen.onkeypress(pads.up, "Up")
screen.onkeypress(pads.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)





screen.exitonclick()