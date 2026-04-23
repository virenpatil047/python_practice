from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def update_lscore(self):
        self.clear()
        self.l_score += 1
        self.goto(-100, 200)
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def update_rscore(self):
        self.clear()
        self.r_score += 1
        self.goto(-100, 200)
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
