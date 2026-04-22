from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('Score: ', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write("Score: ", move=False, align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
