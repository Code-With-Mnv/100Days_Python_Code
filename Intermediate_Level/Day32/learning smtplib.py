import smtplib

email = "codewithmanav70@gmail.com"
password = "sfgy ussm cqcy seps"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(
    from_addr=email,
    to_addrs="manavfun0@gmail.com",
    msg="Hey there buddy! This mai has been sent automatically to you by my Python project!",
)
connection.close()
