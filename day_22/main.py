import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

MAX_GAME_SPEED = 0.006

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

last_spawn = time.time()
game_is_on = True
game_speed = 0.1
cars_spawn_time = 10 * game_speed

while game_is_on:
    
    time.sleep(game_speed)
    screen.update()
    
    if time.time() - last_spawn > cars_spawn_time:
        car_manager.spawn_cars()
        last_spawn = time.time()
    
    car_manager.move_cars()
    
    if car_manager.check_collison(player):
        scoreboard.game_over()
        game_is_on = False
    
    if player.cross_finish_line():
        scoreboard.update()
        if game_speed > MAX_GAME_SPEED:
            game_speed /= 2
            cars_spawn_time = 10 * game_speed

screen.exitonclick()
