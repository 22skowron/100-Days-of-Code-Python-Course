import random
from snake import Snake
from turtle import Turtle, Screen

# canvas = Screen()
# canvas.setup(width=600, height=600)
#################################################################
coordinate_basis = []

x = -280
while x < 281:
    coordinate_basis.append(x)
    x += 20

# print(coordinate_basis)

#################################################################

class Fruits:
    def __init__(self):
        self.fruits_list = []

    def generate_fruit(self):
        fruit = Turtle(shape="square")
        fruit.color("purple")
        rand_x = random.choice(coordinate_basis)
        rand_y = random.choice(coordinate_basis)
        fruit.teleport(rand_x, rand_y)
        self.fruits_list.append(fruit)

    def delete_fruit(self, fruit_position):
        for y in self.fruits_list:
            if fruit_position == y.position():
                y.hideturtle()
                self.fruits_list.remove(y)



#########################################################

# fruit1 = Fruits()
# fruit1.generate_fruit()
# print(fruit1.fruits_list[0].position())

#########################################################


# canvas.exitonclick()