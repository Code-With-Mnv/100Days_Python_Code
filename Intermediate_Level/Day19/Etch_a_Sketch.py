from turtle import Turtle, Screen

turty = Turtle()
window = Screen()


def forward():
    turty.forward(10)


def backward():
    turty.backward(10)


def turn_right():
    turty.right(10)


def turn_left():
    turty.left(10)


def clear_screen():
    window.clear()


window.listen()
window.onkey(key="w", fun=forward)
window.onkey(key="s", fun=backward)
window.onkey(key="a", fun=turn_left)
window.onkey(key="d", fun=turn_right)
window.onkey(key="c", fun=clear_screen)
window.exitonclick()
