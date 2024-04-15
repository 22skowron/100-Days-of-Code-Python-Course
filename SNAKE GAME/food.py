from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed(0)
        self.color("green")
        # self.resizemode("user")
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.generate_food()

    def generate_food(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        if (-100 < rand_x < 100) and (210 < rand_y < 280):
            self.generate_food()
        else:
            self.goto(rand_x, rand_y)


class Brackets:
    def __init__(self):
        for x in range(2):
            bracket = Turtle()
            bracket.penup()
            bracket.color("yellow")
            bracket.teleport(100, 0)
            bracket.resizemode("user")
            bracket.shapesize(stretch_wid=300, stretch_len=0.1)
        bracket.teleport(-100, 0)


