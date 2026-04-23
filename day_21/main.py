import time
from turtle import Screen
from pads import Pads
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Arcade Game")
screen.tracer(0)

pads = Pads()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(pads.r_up, "Up")
screen.onkeypress(pads.r_down, "Down")
screen.onkeypress(pads.l_up, "w")
screen.onkeypress(pads.l_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    ball.move(pads.get_pads(), scoreboard.get_score())





screen.exitonclick()