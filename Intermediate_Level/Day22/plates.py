from turtle import Turtle


class Plates(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_plate(position)

    def create_plate(self, position):
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

