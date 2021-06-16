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

@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
