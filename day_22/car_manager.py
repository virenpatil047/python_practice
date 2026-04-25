import random
from turtle import Turtle, Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
COLLID_DISTANCE = 20
EDGE = 650
SPAWN_RANGE_X = [300, 350]
SPAWN_RANGE_Y = [-250, 250]


class CarManager(Turtle):
    
    def __init__(self):
        self.cars = []
        self.spawn_cars()
    
    def spawn_car(self):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color(random.choice(COLORS))
        turtle.shapesize(stretch_len=2, stretch_wid=1)
        turtle.goto(random.randint(SPAWN_RANGE_X[0], SPAWN_RANGE_X[1]) , random.randint(SPAWN_RANGE_Y[0], SPAWN_RANGE_Y[1]))
        turtle.setheading(180)
        self.cars.append(turtle)
        
    def spawn_cars(self):
        for i in range(0, random.randint(1, 3)):
            self.spawn_car()
        
    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
            
    def check_collison(self, player):
        if any(car.distance(player) < COLLID_DISTANCE for car in self.cars):
            return True
        return False