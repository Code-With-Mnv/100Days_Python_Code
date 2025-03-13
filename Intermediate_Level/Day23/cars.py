from turtle import Turtle
from random import choice, randint

coordinates = []
for i in range(-240, 261, 40):
    coordinates.append((300, i))

colors = ["red", "blue", "green", "orange", "violet", "purple", "cyan", "aquamarine", "chartreuse"]


class Cars:

    def __init__(self):
        self.cars_list = []

    def generate_cars(self):
        gen_ran = randint(0, 6)
        if gen_ran == 5 or gen_ran == 3 or gen_ran == 4:
            car_t = Turtle()
            car_t.shape("square")
            car_t.penup()
            car_t.shapesize(stretch_wid=1, stretch_len=2)
            car_t.color(choice(colors))
            car_t.goto(choice(coordinates))
            self.cars_list.append(car_t)

    def move_cars(self):
        for car_t in self.cars_list:
            new_x = car_t.xcor() - 20
            car_t.goto(new_x, car_t.ycor())

    def reset_cars(self):
        Turtle().clear()
        self.generate_cars()
