from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscores.txt", mode="r") as file:
            lines = file.read()
            self.highscore = int(lines)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.highscore < self.score:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        with open("highscores.txt", mode="w") as file:
            file.write(str(self.highscore))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


