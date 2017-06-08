class Task extends React.Component {
    constructor() {
        super();
        this.state = {
            isDone: false,
        };
    }

    componentWillMount() {
        this.setState({
            isDone: this.props.done
        });
    }

    render() {
        let taskTitle;
        let buttonText;
        if (!this.state.isDone) {
            taskTitle = this.props.title;
            buttonText = 'Done';
        } else {
            taskTitle = <del>{this.props.title}</del>;
            buttonText = 'To-do';
        }

        return (
            <div>
                <p>Title: {taskTitle}</p>
                <p>Description: {this.props.description}</p>
                <div>
                    <button onClick={this._toggleDone.bind(this)}>{buttonText}</button>
                </div>
                <hr />
            </div>
        );
    }

    _toggleDone(event) {
        event.preventDefault();

        if (this.state.isDone == false) {
            this.setState({
                isDone: !this.state.isDone,
                buttonText: 'To-do'
            });
        }
        else {
            this.setState({
                isDone: !this.state.isDone,
                buttonText: 'Done'
            });
        }
        $.ajax({
            url: '/tasks/' + this.props.id,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify({
                done: !this.state.isDone
            }),
            dataType: 'json'
        });
    }
}

class TaskBox extends React.Component {
    constructor() {
        super();
        this.state = {
            tasks: []
        };
    }

    componentWillMount() {
        this._fetchTasks();
    }
    
    render() {
        const tasks = this._getTasks();
        return (
            <div className="task-box">
                <TaskForm addTask={this._addTask.bind(this)}/>
                <h2>Tasks</h2>
                <div className="task-list">
                    {tasks}
                </div>
            </div>
        );
    }

    _getTasks() {
        return this.state.tasks.map((task) => {
            return (<Task
                title={task.title}
                description={task.description}
                id={task.id}
                done={task.done}/>);
        });
    }

    _addTask(taskTitle, taskDescription) {
        let task = {
            id: this.state.tasks.length + 1,
            title: taskTitle,
            description: taskDescription
        };

        this.setState({
            tasks: this.state.tasks.concat([task])
        });
    }

    _fetchTasks() {
        var temp = [];
        var i;
        var blah;
        $.ajax({
            method: 'GET',
            url: '/tasks',
            success: (tasks) => {
                this.setState({tasks})
            }
        });
    }
}

class TaskForm extends React.Component {
    render() {
        return (
            <form onSubmit={this._handleSubmit.bind(this)}>
                <h2>New Task</h2>
                <div className="task-form-fields">
                    <h3>Title:</h3>
                    <input ref={input => this._title = input}/>
                    <h3>Description:</h3>
                    <input ref={input => this._description = input}/>
                </div>
                <div className="task-form-actions">
                    <br />
                    <button type="submit">
                        submit
                    </button>
                </div>
            </form>
        );
    }

    _handleSubmit(event) {
        event.preventDefault();

        if (!this._title.value) {
            alert('Please enter a title.');
            return;
        }

        this.props.addTask(this._title.value, this._description.value);

        $.ajax({
            url: '/tasks',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                title: this._title.value,
                description: this._description.value
            }),
            dataType: 'json'
        });

        this._title.value = '';
        this._description.value = '';
    }
}

ReactDOM.render(<TaskBox />, document.getElementById('content'));