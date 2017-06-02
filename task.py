from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# stores and array of dictionary objects {title: value, description: value}
taskArray = [{'id': 0, 'title': 'title1', 'description': 'description1', 'done': False}]

@app.route('/')
def tasks():
    return render_template('index.html')
  
@app.route('/tasks', methods=['GET'])
def allTasks():
    return jsonify(taskArray)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def singleTask(task_id):
    # treat id as index of taskArray
    for task in taskArray:
        if task['id'] == task_id:
            return jsonify(task)
    return "", 404


@app.route('/tasks', methods=['POST'])
def newTask():
    pass

@app.route('/tasks/<id>', methods=['DELETE'])
def deleteTask():
    pass
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)