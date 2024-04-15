            ###################### IMPORT STATEMENTS
from turtle import Screen
from snake import Snake
from fruits import Fruits
from food import Food, Brackets
from scoreboard import Scoreboard, Highscore
import time
import random

            ###################### CONSTANCE
DELAY = False

    ########################################################################## # # #
def turn_off():
    global is_True
    if is_True == False:
        is_True = True
    elif is_True == True:
        is_True = False


    ########################################################################## # # #


            ###################### CANVAS SETUP
canvas = Screen()
canvas.tracer(0)
canvas.setup(width=600, height=600)
canvas.bgcolor("black")
canvas.title("My Snake Game")

            ###################### OBJECTS
snake = Snake()
food = Food()
scoreboard = Scoreboard(-85, 265)
highscore = Highscore(85, 265)
# brackets = Brackets()
# fruits = Fruits()

            ###################### KEY CONTROL
canvas.listen()

canvas.onkey(fun=snake.turn_left, key="a")
canvas.onkey(fun=snake.turn_right, key="d")
canvas.onkey(fun=snake.turn_north, key="w")
canvas.onkey(fun=snake.turn_south, key="s")
canvas.onkey(fun=turn_off, key="space")


            ###################### DETECT WALL COLLISION
def detect_wall_collision():
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        return True
    else:
        return False


            ###################### DETECT TAIL COLLISION
def detect_tail_collision():
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            return True
        else:
            return False


            ###################### MAIN PROGRAM
is_True = True
while is_True:
    if DELAY:
        canvas.tracer(1)
        scoreboard.game_over()
        canvas.tracer(0)
        scoreboard.add_point(-85, 265)
        snake.set_to_start_position()

        DELAY = False
    canvas.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <= 18:
        scoreboard.clear()
        scoreboard.add_point(-85, 265)
        food.generate_food()
        snake.increase_length()
        if scoreboard.points > highscore.high_score:
            highscore.update_high_score(scoreboard.points)
            with open("variable_storage.txt", mode="w") as document:
                document.write(f"{highscore.high_score}")


    if detect_wall_collision() or detect_tail_collision():
        # scoreboard.game_over()
        time.sleep(1)
        # snake.set_to_start_position()
        scoreboard.points = -1
        # scoreboard.add_point(-85, 265)
        DELAY = True
























canvas.mainloop()