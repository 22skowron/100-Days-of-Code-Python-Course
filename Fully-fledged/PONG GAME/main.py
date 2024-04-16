            ###################### IMPORT STATEMENTS
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Printer, Scoreboard
import time

            ###################### CONSTANCE
DISTANCE = 20
INIT_PADDLE_XCOR = 350
POINTS_IN_GAME = 2  
DELAY = False

    ########################################################################## # # #


    ########################################################################## # # #


            ###################### CANVAS SETUP
canvas = Screen()
canvas.mode("logo")
canvas.setup(width=800, height=600)
canvas.bgcolor("black")
canvas.title("PONG game")

canvas.tracer(0)


            ###################### OBJECTS
left_p = Paddle(-INIT_PADDLE_XCOR)
right_p = Paddle(INIT_PADDLE_XCOR)
ball = Ball()
printer = Printer()
scoreboard = Scoreboard()


            ###################### FUNCTIONS
# def steering_off():
#     canvas.onkeypress(fun=right_p.move_up, key="3")
#     canvas.onkeypress(fun=right_p.move_down, key="3")
#
#     canvas.onkeypress(fun=left_p.move_up, key="3")
#     canvas.onkeypress(fun=left_p.move_down, key="3")
#
#
# def steering_on():
#     canvas.onkeypress(fun=right_p.move_up, key="Up")
#     canvas.onkeypress(fun=right_p.move_down, key="Down")
#
#     canvas.onkeypress(fun=left_p.move_up, key="w")
#     canvas.onkeypress(fun=left_p.move_down, key="s")

def turn_off_game():
    printer.game_finished()
    global round_runs
    round_runs = False

def reset_elements():
    ball.move_to_start_point()
    left_p.initialize_paddles(-INIT_PADDLE_XCOR)
    right_p.initialize_paddles(INIT_PADDLE_XCOR)


            ###################### KEY CONTROL
canvas.listen()

canvas.onkeypress(fun=right_p.move_up, key="Up")
canvas.onkeypress(fun=right_p.move_down, key="Down")

canvas.onkeypress(fun=left_p.move_up, key="w")
canvas.onkeypress(fun=left_p.move_down, key="s")

canvas.onkey(fun=ball.change_heading, key="space")

canvas.onkey(fun=turn_off_game, key="m")

    ########################################################################## # # #



    ########################################################################## # # #


            ###################### MAIN PROGRAM
game_runs = True
round_runs = True

while round_runs:

    canvas.update()
    if DELAY:
        time.sleep(0.5)
        DELAY = False
    time.sleep(0.002)
    ball.move()

    if ball.ycor() >= 290:
        ball.obij_od_sufitu()
    if ball.ycor() <= -290:
        ball.obij_od_podlogi()

    if -332 < ball.xcor() <= -330:
        gora_paletki = left_p.ycor() + 50
        dol_paletki = left_p.ycor() - 50
        if (dol_paletki - 10) < ball.ycor() < (gora_paletki + 10):
            ball.odbij_od_lewej_paletki()

    if 332> ball.xcor() >= 330:
        gora_paletki = right_p.ycor() + 50
        dol_paletki = right_p.ycor() - 50
        if (dol_paletki - 10) < ball.ycor() < (gora_paletki + 10):
            ball.odbij_od_prawej_paletki()

    if ball.xcor() < -420:
        scoreboard.update_R_score()
        reset_elements()
        DELAY = True
    elif ball.xcor() > 420:
        scoreboard.update_L_score()
        reset_elements()
        DELAY = True

    if scoreboard.score_R == POINTS_IN_GAME or scoreboard.score_L == POINTS_IN_GAME:
        ball.hideturtle()
        canvas.tracer(1)
        printer.game_over()
        printer.start_counting()
        scoreboard.reset_scores()
        canvas.tracer(0)
        ball.showturtle()


canvas.update()
canvas.exitonclick()