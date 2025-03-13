import json
import random
import tkinter.messagebox
from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass():
    web_app = web_app_entry.get()
    user_name = username_entry.get()
    nos = "1234567890"
    sym = "@#&"

    web_pass = ""

    for a in range(0, len(web_app) // 2):
        web_pass = web_pass + web_app[a]

    user_pass = ""

    for b in range(0, len(user_name) // 2):
        user_pass = user_pass + user_name[b]

    no = random.choice(nos)

    s = random.choice(sym)

    password = user_pass + no + s + web_pass

    choice = tkinter.messagebox.askyesno(
        title="System Generated Password",
        message=f"Password: {password}\nIf you "
        f"are satisfied with the "
        f"password, click 'YES'\nelse, "
        f"click 'NO'",
    )

    if choice:
        password_entry.insert(0, password)
    else:
        generate_pass()


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    web_app = web_app_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {web_app: {"username": username, "password": password}}

    if password == "" or username == "" or web_app == "":
        tkinter.messagebox.showwarning(
            title="Empty Field", message="Don't leave the fields empty!"
        )
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)

        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)

            tkinter.messagebox.showinfo(
                title="Success", message="The account details have been saved!"
            )

        else:
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

            tkinter.messagebox.showinfo(
                title="Success", message="The account details have been saved!"
            )

        finally:
            web_app_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- VIEW PASSWORD ------------------------------- #


def find_pass():
    web_app = web_app_entry.get()

    found = 0

    with open("data.json", "r") as file:
        data = json.load(file)
        acc = data.keys()

        for i in acc:
            if i == web_app:
                tkinter.messagebox.showinfo(
                    title="Account Found!",
                    message=f"Web/App: {web_app}\nUsername: {data[i]["username"]}\n"
                    f"Password: {data[i]["password"]}",
                )
                found = 1

    if found == 0:
        tkinter.messagebox.showerror(
            title="Account Not Found!", message=f"{web_app} account not found!"
        )


# ---------------------------- UI SETUP ------------------------------- #

# window
root_window = Tk()
root_window.title("PyPassword Manager")
root_window.config(padx=50, pady=50, bg="black")

# canvas
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(column=1, row=0)

# labels
web_app_label = Label(text="Website/App Name: ")
web_app_label.config(fg="cyan", bg="black")
web_app_label.grid(column=0, row=1)

username_label = Label(text="Email/Username: ")
username_label.config(fg="cyan", bg="black")
username_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.config(fg="cyan", bg="black")
password_label.grid(column=0, row=3)

# entries
web_app_entry = Entry(width=40)
web_app_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
web_app_entry.focus()

username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "manavfun0@gmail.com")

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, sticky="EW")

# buttons
gen_pass_button = Button(text="Generate Password", width=18, command=generate_pass)
gen_pass_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=40, command=save_data)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

view_button = Button(text="Find Password", width=40, command=find_pass)
view_button.grid(row=5, column=1, columnspan=2, sticky="EW")

root_window.mainloop()
