from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)
