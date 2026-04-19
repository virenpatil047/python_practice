# from turtle import Turtle, Screen

# turtle = Turtle()
# print(turtle)

# step = 0
# while step != 100:
#     turtle.getscreen()
#     step += 1

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)