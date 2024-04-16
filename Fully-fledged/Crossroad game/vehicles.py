import random
from turtle import Turtle

# totally_random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
# random_color = random.choice(["yellow", "pink", "red", "orange", "green", "purple"])

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car = []
        self.car_segments_coordinates = []
        random_color = random.choice(["yellow", "pink", "red", "orange", "green", "purple"])
        for x in range(3):
            x = Turtle(shape="square")
            x.penup()
            x.color(random_color)
            self.car.append(x)

    def spawn_outside(self):
        y_cor = random.randint(-280, 280)
        x_cor = random.randint(300, 350)
        for x in self.car:
            x.goto(x_cor, y_cor)
            self.car_segments_coordinates.append(x.position())
            x_cor += 20

    def spawn_inside(self):
        # LOSOWE KOORDYNATY, TAK ABY CAR NIE NACHODZIŁ NA ŻÓŁWIA PRZY SPAWNIE
        x_cor = random.randint(-340, 300)
        if -70 < x_cor < 30:
            y_cor = random.randint(-210, 290)
        else:
            y_cor = random.randint(-290, 290)

        for x in self.car:
            x.goto(x_cor, y_cor)
            self.car_segments_coordinates.append(x.position())
            x_cor += 20
        # print(self.car_segments_coordinates)

    def move(self, cars_step):
        for x in self.car:
            x.backward(cars_step)
            index = self.car.index(x)
            self.car_segments_coordinates[index] = x.position()

    def take_off_the_screen(self):
        for x in self.car:
            x.goto(-350, -350)


