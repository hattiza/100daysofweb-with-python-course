from program import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home Page")


@app.route("/100days")
def hundred_days():
    return render_template("100Days.html", title="100 Days of Code")
