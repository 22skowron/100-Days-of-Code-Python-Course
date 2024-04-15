from turtle import Turtle

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")

    def write_game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=('Arial', 20, 'bold'))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.score = 0
        self.goto(-260, 245)
        self.write(arg=f"Score: {self.score}", align="left", font=('Arial', 18, 'bold'))

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align="left", font=('Arial', 18, 'bold'))