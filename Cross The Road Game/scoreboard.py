FONT = ("Courier", 22, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.speed=0.11
        self.update()


    def update(self):
        self.goto(-280, 260)
        self.write(f"Level:{self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.speed*=0.8
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)
