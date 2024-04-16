import time
from turtle import Turtle


class Printer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

        self.zolw1 = Turtle()
        self.zolw1.penup()
        self.zolw1.hideturtle()
        self.zolw1.color("white")

        self.zolw2 = Turtle()
        self.zolw2.penup()
        self.zolw2.hideturtle()
        self.zolw2.color("white")

        self.zolw3 = Turtle()
        self.zolw3.penup()
        self.zolw3.hideturtle()
        self.zolw3.color("white")

        self.zolw4 = Turtle()
        self.zolw4.penup()
        self.zolw4.hideturtle()
        self.zolw4.color("white")

    def start_counting(self):
        self.zolw2.goto(0, -20)

        self.zolw4.goto(0, - 100)
        self.zolw4.write(arg=f"PRESS M TO EXIT", align="center", font=("Arial", 12, "bold"))

        for x in range(4, 0, -1):
            self.zolw2.write(arg=f"New game starts in: {x-1}", align="center", font=("Arial", 17, "normal"))
            time.sleep(1)
            self.zolw2.clear()

        self.zolw4.clear()


    def game_over(self):
        self.zolw1.goto(0, 0)

        self.zolw1.write(arg=f"GAME OVER", align="center", font=("Arial", 15, "bold"))
        time.sleep(1)
        self.zolw1.clear()
        
    def game_finished(self):
        self.zolw2.clear()
        self.zolw2.goto(0, -500)
        self.zolw4.clear()
        self.zolw4.goto(0, -500)

        self.zolw3.goto(0, 0)

        self.zolw3.write(arg=f"FINISHED", align="center", font=("Arial", 40, "bold"))

        time.sleep(2)
        self.zolw3.clear()

scoreboard_turtles = []
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_L = 0
        self.score_R = 0
        self.player_L_score = Turtle()
        self.player_R_score = Turtle()
        scoreboard_turtles.append(self)
        scoreboard_turtles.append(self.player_L_score)
        scoreboard_turtles.append(self.player_R_score)

        for x in scoreboard_turtles:
            x.color("white")
            x.penup()
            x.hideturtle()

        self.goto(0, 260)
        self.write(arg=f"Scoreboard:", align="center", font=("", 14, "normal"))

        self.player_R_score.goto(30, 230)
        self.player_R_score.write(f"{self.score_R}", align="center",font=("", 20, "normal"))
        self.player_L_score.goto(-30, 230)
        self.player_L_score.write(f"{self.score_L}", align="center",font=("", 20, "normal"))

    def update_R_score(self):
        self.player_R_score.clear()
        self.score_R += 1
        self.player_R_score.write(f"{self.score_R}", align="center",font=("", 20, "normal"))

    def update_L_score(self):
        self.player_L_score.clear()
        self.score_L += 1
        self.player_L_score.write(f"{self.score_L}", align="center", font=("", 20, "normal"))

    def reset_scores(self):
        self.score_R, self.score_L = 0, 0
        self.player_L_score.clear()
        self.player_R_score.clear()
        self.player_L_score.write(f"{self.score_R}", align="center", font=("", 20, "normal"))
        self.player_R_score.write(f"{self.score_L}", align="center", font=("", 20, "normal"))

# josh = Scoreboard()
print(scoreboard_turtles)












