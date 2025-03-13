# ------------------------------------ IMPORTS ------------------------------------ #
import random
from tkinter import *

import pandas

# ------------------------------------ GLOBAL VARIABLES ------------------------------------ #
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------ DATA ------------------------------------ #
data_dict = {}
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    print(original_data)
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


# ------------------------------------ FUNCTIONS ------------------------------------ #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)

    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bkg, image=flashcard_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bkg, image=flashcard_back)


def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()


# ------------------------------------- UI ------------------------------------- #
# window
window = Tk()
window.title("FlashCards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# flashcard front
flashcard_front = PhotoImage(file="card_front.png")
flashcard_back = PhotoImage(file="card_back.png")
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
card_bkg = canvas.create_image(400, 265, image=flashcard_front)
title_text = canvas.create_text(400, 150, text="Word", font=("Consolas", 30, "italic"))
word_text = canvas.create_text(
    400,
    350,
    text="Text",
    font=("Consolas", 30, "bold"),
)
canvas.grid(row=0, column=0, columnspan=2)

# right button
right_pic = PhotoImage(file="right.png")
right_button = Button(
    image=right_pic,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=next_card,
)
right_button.grid(column=0, row=1)

# left button
wrong_pic = PhotoImage(file="wrong.png")
wrong_button = Button(
    image=wrong_pic,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=is_known,
)
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()
