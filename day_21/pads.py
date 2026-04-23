from turtle import Turtle

MAX_Y_COR = 300
MOVE = 60
SIDE = 350

class Pads(Turtle):
    
    def __init__(self):
        self.pads = []
        self.create_pad(-SIDE)
        self.create_pad(SIDE)
        self.left_pad = self.pads[0]
        self.right_pad = self.pads[1]
    
    def create_pad(self, side):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.turtlesize(stretch_len=1, stretch_wid=5)
        turtle.color("white")
        turtle.goto(side, 0)
        self.pads.append(turtle)
    
    def r_up(self):
        x_cor, y_cor = self.right_pad.xcor(), self.right_pad.ycor()
        if y_cor + MOVE < MAX_Y_COR:
            self.right_pad.goto(x_cor, y_cor + MOVE)

    def r_down(self):
        x_cor, y_cor = self.right_pad.xcor(), self.right_pad.ycor()
        if abs(y_cor - MOVE) < MAX_Y_COR:
            self.right_pad.goto(x_cor, y_cor - MOVE)

    def l_up(self):
        x_cor, y_cor = self.left_pad.xcor(), self.left_pad.ycor()
        if y_cor + MOVE < MAX_Y_COR:
            self.left_pad.goto(x_cor, y_cor + MOVE)

    def l_down(self):
        x_cor, y_cor = self.left_pad.xcor(), self.left_pad.ycor()
        if abs(y_cor - MOVE) < MAX_Y_COR:
            self.left_pad.goto(x_cor, y_cor - MOVE)
            
    def get_pads(self):
        return self.pads
