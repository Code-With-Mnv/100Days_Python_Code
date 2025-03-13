from turtle import Turtle, Screen
from random import choice

window = Screen()
window.setup(width=1000, height=500)
user_bet = window.textinput(title="Make a Bet!", prompt="Which turtle is gonna win? Enter the color: ")

colors = ["red", "orange", "cyan", "green", "blue", "purple", "brown"]
dist = [5, 10, 15, 20]
y_coor = [0, -40, 40, -80, 80, -120, 120]
all_turtles = []

for i in range(0, 7):
    turty = Turtle()
    turty.shape("turtle")
    turty.penup()
    turty.color(colors[i])
    turty.goto(x=-500, y=y_coor[i])
    all_turtles.append(turty)

is_over = False

while not is_over:
    for turtles in all_turtles:
        run = choice(dist)
        turtles.forward(run)

    for turtles in all_turtles:
        if turtles.xcor() == 500:
            if turtles.pencolor().lower() == user_bet.lower():
                print(f"You've won! {user_bet} turtle won the race!")
                is_over = True
            else:
                print(f"You've lost! {turtles.pencolor()} turtle has won the race!")
                is_over = True


window.exitonclick()
