from turtle import Turtle, Screen
import pandas

window = Screen()
turty = Turtle()
turty.penup()
turty.hideturtle()
turty.pencolor("black")
window.setup(1200, 700)
window.title("U.S. STATES GAME")
window.bgpic("us_blank_map.gif")

states_coor = {}
states = []
x_coors = []
y_coors = []
guessed_states = []

data = pandas.read_csv("50_states_data.csv")

for i in data["state"]:
    states.append(i)

for j in data["x"]:
    x_coors.append(j)

for k in data["y"]:
    y_coors.append(k)

a = 0
while a < 50:
    coors = (x_coors[a], y_coors[a])
    states_coor[states[a]] = coors
    a += 1

score = 0

while len(guessed_states) < 50:
    guess = window.textinput(f"{score}/50 guessed", "Enter the name of a state: ")
    if guess.title() in states:
        turty.goto(states_coor[guess])
        turty.pendown()
        turty.write(guess, False, "center", ("Consolas", 12, "normal"))
        turty.penup()
        score += 1
        guessed_states.append(guess)

    if guess.title() == "Exit":
        remaining_states = [state for state in states if state not in guessed_states]
        df = pandas.DataFrame(remaining_states)
        df.to_csv("remaining_states.csv")
        break

    if guess.capitalize() not in states_coor.keys():
        continue

    if len(guessed_states) == 49:
        print("You have guessed all the states! Congrats!")
