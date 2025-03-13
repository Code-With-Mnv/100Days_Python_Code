# importing the modules
from tkinter import *

# declaring the global variables
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK = 10
LONG_BREAK = 30
WORK_SETS = 0
timer = None


# define the start_timer and reset_timer function and connect it with button
def start_timer():
    global WORK_SETS
    WORK_SETS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK * 60

    if WORK_SETS in (1, 3, 5, 7):
        count_down(work_sec)
        head_label.config(text="WORK")
    elif WORK_SETS in (2, 4, 6):
        count_down(short_break_sec)
        head_label.config(text="SHORT BREAK")
    elif WORK_SETS == 8:
        count_down(long_break_sec)
        head_label.config(text="LONG BREAK")
    else:
        reset_timer()


def reset_timer():
    window.after_cancel(timer)
    global WORK_SETS
    WORK_SETS = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    head_label.config(text="TIMER")


# define the count_down function to run the timer
def count_down(secs):
    mins = secs // 60
    sec = secs % 60

    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{mins}:{sec}")

    if secs > 0:
        global timer
        timer = window.after(1000, count_down, secs - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = WORK_SETS // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# create a UI
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

head_label = Label(text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
head_label.grid(row=0, column=1)

canvas = Canvas(width=202, height=227, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(102, 114, image=tomato_pic)
timer_text = canvas.create_text(102, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", bg=PINK, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=PINK, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()
