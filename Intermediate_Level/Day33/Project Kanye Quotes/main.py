# imports

import tkinter as tk

import requests

# globals

WINDOW_BKG = "white"
TEXT_COLOR = "black"


# API


def show_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=quote)


# GUI

window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=20, pady=20, bg=WINDOW_BKG)

text_box_img = tk.PhotoImage(file="background.png")
canvas = tk.Canvas(width=310, height=420, bg=WINDOW_BKG, highlightthickness=0)
canvas.create_image(155, 210, image=text_box_img)
quote_text = canvas.create_text(
    155,
    210,
    text="Kanye Quote goes here!",
    width=250,
    fill=TEXT_COLOR,
    font=("Consolas", 20, "italic"),
)
canvas.grid(column=0, row=0)

kanye_pic = tk.PhotoImage(file="kanye.png")
button = tk.Button(
    image=kanye_pic, bg=WINDOW_BKG, highlightthickness=0, command=show_quote
)
button.grid(column=0, row=1)

window.mainloop()
