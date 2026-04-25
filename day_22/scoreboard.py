from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'
POSITION = (-220, 260)

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.write("Level: 1", move=False, align=ALIGNMENT, font=FONT)
        
    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", move=False, align=ALIGNMENT, font=FONT)
