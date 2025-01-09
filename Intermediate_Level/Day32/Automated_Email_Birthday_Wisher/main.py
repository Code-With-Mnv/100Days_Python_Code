# imports

import datetime as dt
import random
import smtplib

import pandas as pd

# globals

EMAIL_ID = "codewithmanav70@gmail.com"
PASSWORD = "sfgy ussm cqcy seps"

# access the dates and months

user_data = pd.read_csv("dob_mail_name_data.csv", skiprows=[11, 12])
user_data_dict = user_data.to_dict("records")

# check for birthday

date_time = dt.datetime.now()
month = date_time.month
day = date_time.day

for data_dict in user_data_dict:

    if data_dict["month"] == month and data_dict["day"] == day:
        gender = data_dict["gender"]
        name = data_dict["name"]
        email_id = data_dict["email_id"]
        me = "Manav"
        # setting up smtp server

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user=EMAIL_ID, password=PASSWORD)

        wishes = ""

        if gender == "M":
            with open("Wishes_for_guyss.txt", "r") as mfile:
                wish_list = mfile.readlines()
                wishes = random.choice(wish_list)

        else:
            with open("Wishes_for_gurlls.txt", "r") as gfile:
                wish_list = gfile.readlines()
                wishes = random.choice(wish_list)

        msg = f"Subject: Celebrating you today!\n\nHeyy {name}\n{wishes}\nCheers,\n{me}"

        server.sendmail(msg=msg, from_addr=EMAIL_ID, to_addrs=email_id)

        print(f"Birthday wishes has been sent to {name}")
