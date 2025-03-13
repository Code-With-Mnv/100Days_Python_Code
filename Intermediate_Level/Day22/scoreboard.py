from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.hideturtle()
        self.color("white")
        self.score = 0

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, False, "center", ("Arial", 30, "normal"))

