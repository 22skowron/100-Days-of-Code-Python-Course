from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, init_xcor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.initialize_paddles(init_xcor)

    def initialize_paddles(self, init_xcor):
        self.goto(init_xcor, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + DISTANCE)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - DISTANCE)