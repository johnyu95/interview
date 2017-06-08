Problem Definition: Build a to-do application with separate front-end and backend components.

Time Constraints: Please spend no more than two hours on this exercise. If you are unable to complete the exercise in the allotted time, please note that in the README and explain what steps you would take to complete the application.

Backend:
	The backend should expose a simple REST API with the following endpoints:
-	GET /tasks: Returns all tasks in the database
-	GET /tasks/<id>: Returns a single task from the database
-	POST /tasks: Returns the ID of a newly created task
-	PATCH /tasks/<id>: Returns the ID of the updated task
-	DELETE: /tasks/<id>: Deletes the specified task from the database

A task has the following schema:
	{
		id: INTEGER,
		title: STRING,
		description: string,
		done: BOOLEAN
	}

Your application should be built using the Flask framework and use a SQLite database to store the tasks for persistence. You can use an ORM to manage the database objects. 

Frontend:
The frontend should be built using React.JS. You should not use Redux or any other state management library. If you do, please provide an explanation in the README file.

	UI Requirements
-	Users should be presented with a list of all of their tasks upon opening the web page. 
-	The top of the page should have a form that allows users to create a new task with title and description.
-	Tasks that have not been completed should show the title and description and a button that allows users to mark them as done.
-	Tasks that have been completed should have a title that is crossed out and a button that allows the user to mark them as to-do.

Name: Jonathan Yu
Description: I started this application by creating a simple flask app for the backend. At first I set up the API endpoints and tested the data using an array of python dictionaries to represent my data.
After that I implemented a sqlite database to store my task entries using SQL-Alchemy. Then I created my frontend using ReactJS. I started by outlining what components would be needed which are
a TaskBox component as the base for the entire application, a Task component to represent a single row of a task, and a TaskForm component which would allow the user to fill out a form to add new tasks.
After the frontend components were set up I connected the frontend and backend using AJAX calls to reach my API endpoints in order to create, update, and delete tasks.

Question 1: If I had one week to update this application I would add a delete button for each individual task as well as a delete all button. I would add these delete features so that it can make
use of the DELETE request endpoint that the backend has as help reduce clutter on the screen for a better user experience. Along with that I would add a "star" button so that the user can flag important
tasks on the list. Lastly I would add a "sort by" button so the user can sort the tasks by newest or oldest task. I think these features would provide a much better user experience.

Question 2: The hardest part of this application was implementing the frontend because I have limited experience using React. Rendering the components seems straight forward but understanding the use
of props and states were a major factor in this application. I overcame this challenge by doing lots of research and looking up tutorials online which helped guide me through the basics of React.