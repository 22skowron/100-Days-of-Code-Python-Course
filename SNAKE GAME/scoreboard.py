from turtle import Turtle
import time
with open("variable_storage.txt", mode="r") as document:
    HIGH_SCORE = int(document.read())

class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        self.points = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(arg=f"Scoreboard: {self.points}", align="center", font=("Arial", 18, "bold"))

    def add_point(self, x_cor, y_cor):
        self.clear()
        self.goto(x_cor, y_cor)
        self.points += 1
        self.write(arg=f"Scoreboard: {self.points}", align="center", font=("Arial", 18, "bold"))



    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Arial", 12, "bold"))
        time.sleep(2)
        self.clear()


class Highscore(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.high_score = HIGH_SCORE
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(arg=f"Highscore: {self.high_score}", align="center", font=("Arial", 18, "bold"))

    def update_high_score(self, new_high_score):
        self.clear()
        self.high_score = new_high_score
        self.write(arg=f"Highscore: {self.high_score}", align="center", font=("Arial", 18, "bold"))