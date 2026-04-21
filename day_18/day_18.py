from turtle import Turtle, Screen

# tim = Turtle()
#tim.shape("turtle")
# tim.color("olive drab")

# Sqaure
# for i in range(1, 5):
#     tim.forward(100)
#     tim.right(90)

# Dash line
# for _ in range(50):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")


# Multiple shapes
# import random
# colours = [
#     "CornflowerBlue",
#     "DarkOrchid",
#     "IndianRed",
#     "DeepSkyBlue",
#     "LightSeaGreen",
#     "wheat",
#     "SlateGray",
#     "SeaGreen",
# ]

# def shape(sides):
#     for side in range(1, sides + 1):
#         tim.forward(100)
#         tim.right(360 / sides)
        
# for n_sides in range(3, 11):
#     tim.color(random.choice(colours))
#     shape(n_sides)


# Random walk
import random
# angle = [90, 180, 270, 360]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r/255, g/255, b/255)

# pen = Turtle()
# pen.pensize(7)
# pen.hideturtle()
# pen.speed(10)
# while True:
#     pen.color(random_color())
#     pen.setheading(random.choice(angle))
#     pen.forward(15)


# Spiral
turtle = Turtle()
turtle.speed('fastest')
degree = 0
while degree <= 360:
    turtle.color(random_color())
    turtle.setheading(degree)
    turtle.circle(100)
    degree += 6




screen = Screen()
screen.exitonclick()
