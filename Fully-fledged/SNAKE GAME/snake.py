from turtle import Turtle, Screen
START_x = 0
START_y = 0
DISTANCE = 20

# canvas = Screen()
# canvas.bgcolor("black")

class Snake:
    LENGTH = 3
    def __init__(self):
        self.all_segments = []
        self.create_snake()

    def detect_tail_collision(self):
        for segment in self.all_segments[1:]:
            if self.head.distance(segment) < 10:
                return True
            else:
                return False

    def create_snake(self):
        x, y = START_x, START_y
        for n in range(Snake.LENGTH):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(x, y)
            x -= 20
            self.all_segments.append(new_segment)
            self.head = self.all_segments[0]

    def move(self):
        for x in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[x - 1].xcor()
            new_y = self.all_segments[x - 1].ycor()
            self.all_segments[x].goto(new_x, new_y)
        self.all_segments[-1].showturtle()
        self.head.forward(DISTANCE)

    def set_to_start_position(self):
        for x in range(len(self.all_segments)-1, -1, -1):
            self.all_segments[x].hideturtle()
            self.all_segments.pop(x)
        self.create_snake()


    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def turn_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def increase_length(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.hideturtle()
        self.all_segments.append(new_segment)

###########################################################
# def increase_length():
#     global LENGTH
#     LENGTH += 1
# snake1 = Snake()
# snake2 = Snake()
#
# print(Snake.LENGTH)
# print(snake1.LENGTH)
# print(snake2.LENGTH)
# print("\n")
#
# Snake.LENGTH = 7
#
# print(Snake.LENGTH)
# print(snake1.LENGTH)
# print(snake2.LENGTH)

# canvas.exitonclick()




