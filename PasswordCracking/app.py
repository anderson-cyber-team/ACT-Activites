from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success")
def landing_page():
    return render_template("landing-page.html")
