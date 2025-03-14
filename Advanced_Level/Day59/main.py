import smtplib

import requests
from flask import Flask
from flask import render_template
from flask import request

posts = requests.get("https://api.npoint.io/89ed75422cc1d4070f35").json()

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", all_posts=posts)


@app.route("/index.html")
def go_to_home():
    return render_template("index.html", all_posts=posts)


@app.route("/about.html")
def go_to_about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("OWN_EMAIL", "OWN_PASSWORD")
        connection.sendmail("OWN_EMAIL", "OWN_EMAIL", email_message)


if __name__ == "__main__":
    app.run(debug=True)
