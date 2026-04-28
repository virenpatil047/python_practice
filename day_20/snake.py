from turtle import Turtle

LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        x_index = 0
        for i in range(0, 3):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.color("white")
            segment.goto(x_index, 0)
            self.segments.append(segment)
            x_index -= 20
    
    def extend(self):
        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(self.segments[-1].position())
        self.segments.append(segment)
        
    def reset(self):
        for segment in self.segments:
            segment.goto(-1500, -1500)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        
            
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].xcor(), self.segments[i-1].ycor())
        self.head.forward(20)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)
