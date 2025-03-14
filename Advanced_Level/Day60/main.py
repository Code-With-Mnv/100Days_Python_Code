from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def start_app():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def fetch_data():
    name = request.form["username"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
