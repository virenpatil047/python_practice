# import colorgram

# colors = colorgram.extract(r'C:\Users\viren\OneDrive\Documents\GitHub\python_practice\day_18\hirst spot\hirst_spot.jpg', 20)
# color_list = []

# def get_color(color):
#     r = color.rgb.r / 256
#     g = color.rgb.g / 256
#     b = color.rgb.b / 256
#     return (r, g, b)

# for color in colors:
#     color_list.append(get_color(color))

# print(color_list)

from turtle import Turtle, Screen
import random

color_list = [(0.92578125, 0.98046875, 0.95703125), (0.97265625, 0.890625, 0.06640625), (0.83203125, 0.05078125, 0.03515625), (0.7734375, 0.046875, 0.13671875), (0.90234375, 0.890625, 0.01953125), (0.76953125, 0.26953125, 0.078125), (0.12890625, 0.3515625, 0.734375), (0.16796875, 0.828125, 0.27734375), (0.9140625, 0.578125, 0.15625), (0.12890625, 0.1171875, 0.59375), (0.0625, 0.0859375, 0.21484375), (0.2578125, 0.03515625, 0.19140625), (0.9375, 0.95703125, 0.98046875), (0.953125, 0.15234375, 0.58203125), (0.25390625, 0.7890625, 0.89453125), (0.0546875, 0.80078125, 0.8671875), (0.24609375, 0.08203125, 0.0390625), (0.875, 0.07421875, 0.43359375)]
turtle = Turtle()
turtle.hideturtle()
turtle.penup()

def draw_dots():
    for i in range(0, 10):
        turtle.dot(10)
        color = random.choice(color_list)
        turtle.color(color[0], color[1], color[2])
        turtle.forward(20)


y = 20
for i in range(0,10):
    draw_dots()
    turtle.setx(0)
    turtle.sety(y)
    y += 20


screen = Screen()
screen.exitonclick()