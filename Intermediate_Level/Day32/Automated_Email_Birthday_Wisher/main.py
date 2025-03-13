import datetime as dt
import random
import smtplib

import pandas as pd

# Email credentials (Consider using environment variables for security)
EMAIL_ID = "manavfun0@gmail.com"
PASSWORD = "fun@mail"  # Use an App Password instead of your actual password.

# Read user data from CSV
user_data = pd.read_csv("dob_mail_name_data.csv")  # Removed skiprows for safety
user_data_dict = user_data.to_dict("records")

# Get current date
date_time = dt.datetime.now()
month = date_time.month
day = date_time.day

# Check for birthdays
for data_dict in user_data_dict:
    if data_dict["month"] == month and data_dict["day"] == day:
        name = data_dict["name"]
        email_id = data_dict["email_id"]
        gender = data_dict["gender"]
        me = "Manav"

        # Select a random wish based on gender
        wish_file = "Wishes_for_guyss.txt" if gender == "M" else "Wishes_for_gurlls.txt"
        with open(wish_file, "r") as file:
            wishes = random.choice(file.readlines()).strip()

        # Email message
        subject = "Subject: Celebrating you today!\n\n"
        body = f"Hey {name},\n\n{wishes}\n\nCheers,\n{me}"
        msg = subject + body

        # Sending email
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ID, PASSWORD)
                server.sendmail(
                    from_addr=EMAIL_ID, to_addrs="codewithmanav70@gmail.com", msg=msg
                )
            print(f"🎉 Birthday wishes sent to {name} ({email_id})")
        except Exception as e:
            print(f"⚠️ Error sending email to {name}: {e}")
