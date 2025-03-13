import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/ang/<name>")
def ang(name):
    gresponse = requests.get(f"https://api.genderize.io?name={name}")
    gdata = gresponse.json()
    gender = gdata["gender"]

    aresponse = requests.get(f"https://api.agify.io?name={name}")
    adata = aresponse.json()
    age = adata["age"]

    return render_template("main.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
