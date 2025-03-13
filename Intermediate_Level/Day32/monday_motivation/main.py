import datetime as dt
import random
import smtplib

MY_EMAIL = "codewithmanav70@gmail.com"
MY_PASSWORD = "sfgy ussm cqcy seps"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    all_quotes.remove(quote)
    with open("quotes.txt", "w") as quote_file:
        quote_file.writelines(all_quotes)

    with open("email_add.txt", "r") as efile:
        email_ids = efile.readlines()

    for email_id in email_ids:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email_id,
                msg=f"Subject:Monday Motivation\n\n{quote}",
            )
