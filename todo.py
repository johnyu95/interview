import os
from flask import Flask, render_template, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    done = db.Column(db.Boolean())

    def __repr__(self):
        return '<Task %r>' % self.title


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

  
@app.route('/tasks', methods=['GET'])
def all_tasks():
    tasks = Task.query.filter_by().all()
    task_array = []
    for task in tasks:
        task_json = {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}
        task_array.append(task_json)
    return jsonify(task_array)


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    task_json = {'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done}
    return jsonify(task_json)


@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        print(request.form['title'])
        abort(400)
    task = Task(title=request.json['title'], description=request.json.get('description', ""), done=False)
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id}), 201


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.done = request.json.get('done', task.done)
    db.session.add(task)
    db.session.commit()
    return jsonify({'id': task.id})


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task is None:
        abort(404)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})
    
    
if __name__ == '__main__':
    db.create_all()
    app.run()
