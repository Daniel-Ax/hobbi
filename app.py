import datetime

from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    completed=db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    completed = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route("/")
def init():
    return "Weolcome to the index page"


@app.route("/hi/")
def who():
    return "Who are you?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"

sqlalchemy.__version__