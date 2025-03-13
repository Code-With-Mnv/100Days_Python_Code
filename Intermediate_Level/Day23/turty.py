from turtle import Turtle


class Turty(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.speed("fastest")

    def move(self):
        new_y = self.ycor() + 20
        self.goto(0, new_y)

    def go_to_start(self):
        self.goto(0, -280)
