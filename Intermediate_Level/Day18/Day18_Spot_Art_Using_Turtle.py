import turtle as t
import random as r
import color_data as cd

turty = t.Turtle()
turty.speed("fastest")


def dotted_line():
    b = 0
    while b <= 10:
        turty.pendown()
        turty.dot(17, r.choice(cd.colors))
        turty.penup()
        turty.forward(35)
        b += 1


def art():
    a = 0
    y = -50
    while a < 10:
        turty.penup()
        turty.goto(0, y)
        dotted_line()
        y += 35
        a += 1


art()
