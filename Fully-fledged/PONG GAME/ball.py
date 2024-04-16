import random
from turtle import Turtle

DISTORTION = 8

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        rand_angle = random.choice([random.randint(30, 150), random.randint(210, 330)])
        self.setheading(rand_angle)

    def move_to_start_point(self):
        self.goto(0, 0)
        rand_angle = random.choice([random.randint(30, 150), random.randint(210, 330)])
        self.setheading(rand_angle)

    def move(self):
        self.forward(1)


    def obij_od_sufitu(self):
        if 0 < self.heading() < 90:
            # nowe nachylenie (90, 180)

            new_direction = 180 - self.heading()
            if 105 < new_direction < 165:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)
        elif 270 < self.heading() < 360:
            # nowe nachylenie (180, 270)

            new_direction = 270 - (self.heading() - 270)
            if 195 < new_direction < 255:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)


    def obij_od_podlogi(self):
        if 90 < self.heading() < 180:
            # nowe nachylenie (0, 90)

            new_direction = 90 - (self.heading() - 90)
            if 15 < new_direction < 75:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)
        elif 180 < self.heading() < 270:
            # nowe nachylenie (270, 360)

            new_direction = 360 - (self.heading() - 180)
            if 285 < new_direction < 345:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)


    def change_heading(self):
        # rand_direction = random.randint(0, 90)
        self.setheading(self.heading() - 180)


    def odbij_od_lewej_paletki(self):
        if 180 < self.heading() < 270:
            # nowe nachylenie (90, 180)

            new_direction = 90 + (270 - self.heading())
            if 105 < new_direction < 165:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)
        elif 270 < self.heading() < 360:
            # nowe nachylenie (0, 90)

            new_direction = 90 - (self.heading() - 270)
            if 105 < new_direction < 165:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)

    def odbij_od_prawej_paletki(self):
        if 0 < self.heading() < 90:
            # nowe nachylenie (270, 360)

            new_direction = 270 + (90 - self.heading())
            if 285 < new_direction < 355:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)
        elif 90 < self.heading() < 180:
            # nowe nachylenie (180, 270)

            new_direction = 270 - (self.heading() - 90)
            if 195 < new_direction < 2555:
                distortion = random.randint(-DISTORTION, DISTORTION)
                new_direction += distortion
            self.setheading(new_direction)














