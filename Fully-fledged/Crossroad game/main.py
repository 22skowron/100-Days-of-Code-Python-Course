            ###################### IMPORT STATEMENTS
from turtle import Turtle, Screen
from vehicles import Car
from scoreboard import GameOver, Scoreboard
import time
import random

            ###################### CONSTANCE
GORGE_SPAWN_POINT = (0, -250)
CARS_INSIDE = 10
CARS_STEP = 10
GORGE_STEP = 10
INITIAL_SPEED = 0.1
INCREMENT = 2

speed = INITIAL_SPEED   #not so constant :)

    ########################################################################## # # #


    ########################################################################## # # #


            ###################### CANVAS SETUP
canvas = Screen()
canvas.setup(width=600, height=600)
canvas.tracer(0)
canvas.colormode(255)
canvas.listen()


            ###################### OBJECTS SETUP
gorge = Turtle(shape="turtle")
gorge.setheading(90)
gorge.penup()
gorge.goto(GORGE_SPAWN_POINT)

cars_list = []
# for x in range(CARS_INSIDE):
#     car = Car()
#     car.spawn_inside()
#     cars_list.append(car)

game_over = GameOver()

scoreboard = Scoreboard()


            ###################### FUNCTIONS
def spawn_cars_inside():
    for x in range(CARS_INSIDE):
        car = Car()
        car.spawn_inside()
        cars_list.append(car)
def spawn_cars_outside():
    if random.randint(1, 10) == 1:
        car = Car()
        car.spawn_outside()
        cars_list.append(car)

def move_gorge():
    gorge.setheading(90)
    gorge.forward(GORGE_STEP)

def move_gorge_right():
    gorge.setheading(0)
    gorge.forward(GORGE_STEP)

def move_gorge_left():
    gorge.setheading(180)
    gorge.forward(GORGE_STEP)

def detect_collision():
    for car in cars_list:
        #deletes redundant cars
        if car.car_segments_coordinates[2][0] < -310:   #to se if works, change -310 to e.g. -100
            cars_list.remove(car)

        #detects collision
        for position in range(2):
            if gorge.distance(car.car_segments_coordinates[position]) < 20:
                return True

def initialize_new_round(action):
    global cars_list
    gorge.goto(GORGE_SPAWN_POINT)
    for car in cars_list:
        car.take_off_the_screen()
    cars_list = []

    if action == "continue_faster":
        global speed
        speed /= INCREMENT

        canvas.update()
        time.sleep(1)
        spawn_cars_inside()
        canvas.update()
        time.sleep(1)

        gorge.goto(GORGE_SPAWN_POINT)       # repeated cause people spam SPACE
    elif action == "restart":
        speed = INITIAL_SPEED
        scoreboard.score = -1
        scoreboard.add_point()

        canvas.update()
        time.sleep(1)
        spawn_cars_inside()

        gorge.goto(GORGE_SPAWN_POINT)       # repeated cause people spam SPACE
    global round_runs
    round_runs = True



            ###################### KEY CONTROL
canvas.onkeypress(fun=move_gorge, key="space")
canvas.onkeypress(fun=move_gorge, key="w")
canvas.onkeypress(fun=move_gorge_left, key="a")
canvas.onkeypress(fun=move_gorge_right, key="d")




    ########################################################################## # # #
# for x in range(3):
#     spawn_cars_outside()
#     print(cars_list)



    ########################################################################## # # #


            ###################### MAIN PROGRAM
game_runs = True
round_runs = True
spawn_cars_inside()

while game_runs:
    while round_runs:
        canvas.update()
        time.sleep(speed)
        spawn_cars_outside()
        for x in cars_list:
            x.move(CARS_STEP)

        if detect_collision():      #also deletes redundant cars, with xcor < -310
            game_over.write_game_over()
            canvas.update()
            time.sleep(1)
            game_over.clear()
            initialize_new_round(action="restart")

        if gorge.ycor() >= 290:
            scoreboard.add_point()
            time.sleep(1)
            initialize_new_round(action="continue_faster")






canvas.exitonclick()

