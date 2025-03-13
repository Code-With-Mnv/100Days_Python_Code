from turtle import Screen, Turtle
from plates import Plates
from pong import Pong
from scoreboard import ScoreBoard

window = Screen()
window.setup(1200, 700)
window.bgcolor("black")
window.title("PyPong")
win_turtle = Turtle()
win_turtle.color("white")
win_turtle.penup()
win_turtle.hideturtle()
win_turtle.goto(0, 300)
win_turtle.write("PyPong", False, "center", ("Arial", 30, "normal"))

r_plate = Plates((570, 0))
l_plate = Plates((-580, 0))
ball = Pong()
right_score = ScoreBoard((300, 310))
left_score = ScoreBoard((-300, 310))

window.listen()
window.onkey(fun=l_plate.up, key="w")
window.onkey(fun=l_plate.down, key="s")
window.onkey(fun=r_plate.up, key="o")
window.onkey(fun=r_plate.down, key="l")

is_game_over = False

while not is_game_over:
    window.update()
    ball.move_ball()

    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.collision_up_down()

    if ball.distance(r_plate) < 50 and ball.xcor() > 320 or ball.distance(l_plate) < 50 and ball.xcor() < -320:
        ball.collision_left_right()

    if ball.xcor() > 600:
        left_score.increase_score()
        ball.reset_ball()

    if ball.xcor() < -600:
        right_score.increase_score()
        ball.reset_ball()

# updating scoreboard

window.exitonclick()
