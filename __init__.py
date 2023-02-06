#!/usr/bin/env python3

from flask import Flask, render_template
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
# from flask_sqlalchemy import SQLAchemy
from datetime import datetime

# Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "123"

# Create a Form Class
class nameform(FlaskForm):
    name = StringField("What's your name", validator=[DataRequired()])
    age = StringField("What's your age", validator=[DataRequired()])
    email = StringField("What's your e-mail", validator=[DataRequired()])
    submit = SubmitField("Submit") 

# Database
#app.config[]

#db = SQLAchemy(app)
# Create Model
#class Users(db.Model): 
#    id =db.Column (db.IntegerField 


# Create a "home" route decorater
@app.route('/')
def index():
    return render_template("index.html")
#@app.route('/user/<name>')
#def user(name):
#    return render_template("user.html", user_name=name) # this returns gives us all the returned variables from the function user. At the same time, the variable comes from the route.

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)

# Custom Error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route('/user/<name>', methods=['GET', 'POST'])
def name():
    name = None
    form = nameform()
    #validate From
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    
    return render_template("name.html", user_name=name, form=form)