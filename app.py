from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Reservation %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    db.create_all()
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = User(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your reservation'

    else:
        tasks = User.query.order_by(User.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = User.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that reservation'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = User.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating reservation'

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":

    app.run(debug=True)