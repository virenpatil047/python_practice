from turtle import Turtle
import time
MOVE = 10

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle") 
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        
    def check_collide(self, pads, score):
        x_cor, y_cor = self.xcor(), self.ycor()
        if abs(x_cor) > 320:
            if min(self.distance(pads[0]), self.distance(pads[1])) <= 50:
                self.move_x = -self.move_x
            elif abs(x_cor) > 370:
                score.update_lscore() if x_cor < 0 else score.update_rscore()
                time.sleep(0.5)
                self.goto(0, 0)
                self.move_x = -self.move_x
                self.move_y = -self.move_y
                return
        if abs(y_cor) > 280:
            self.move_y = -self.move_y
        
    def move(self, pads, score):
        self.check_collide(pads, score)
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)