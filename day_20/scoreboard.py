from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('Score: ', 15, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", move=False, align=ALIGNMENT, font=FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = -1
        self.update_score()
