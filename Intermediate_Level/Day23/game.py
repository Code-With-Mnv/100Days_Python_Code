from turtle import Screen
from turty import Turty
from cars import Cars
import time
from levels import Scoreboard

window = Screen()
window.setup(600, 600)
window.title("PyTurtle Crossing")

crossing_turtle = Turty()
moving_cars = Cars()
scoreboard = Scoreboard()
window.tracer(0)

window.listen()
window.onkey(key="w", fun=crossing_turtle.move)

is_game_over = False

while not is_game_over:
    time.sleep(0.1)
    window.update()

    moving_cars.generate_cars()

    moving_cars.move_cars()

    for i in moving_cars.cars_list:
        if crossing_turtle.distance(i) <= 25 or crossing_turtle.distance(i) <= 7:
            scoreboard.game_over()
            is_game_over = True

        if crossing_turtle.ycor() > 280:
            scoreboard.increase_level()
            crossing_turtle.go_to_start()

window.exitonclick()
