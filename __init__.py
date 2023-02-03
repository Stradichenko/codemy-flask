#!/usr/bin/env python3

from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)

# Create a "home" route decorater
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name) # this returns gives us all the returned variables from the function user. At the same time, the variable comes from the route.


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)

# Custom Error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
