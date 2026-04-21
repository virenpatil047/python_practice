from turtle import Turtle, Screen

# White board
screen = Screen()

# degree = 0

# def move_forwards():
#     tim.forward(10)
    
# def counter_clock():
#     tim.left(10)

# def move_backwards():
#     tim.backward(10)

# def clock():
#     tim.right(10)

# def clear():
#     tim.home()
#     tim.clear()

# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="a", fun=counter_clock)
# screen.onkey(key="d", fun=clock)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="c", fun=clear)
# screen.listen()


# Turtle race
import random

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_index = -200
for i in range(0, 6):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    y_index += 60
    turtles[i].goto(x=-230, y=y_index)

is_on = True
while is_on:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            if user_bet == turtle.pencolor():
                print(f"You've won! The {turtle.color()[0]} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.color()[0]} turtle is the winner!")
            is_on = False
        
    
screen.exitonclick()