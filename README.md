# My Kanban Board

My Kanban Board is a powerful tool to manage your day to day tasks. The main web application is divided into three boards (ToDo, Doing, Done). Also, My Kanban Board includes a login system to provide secure and personalized data access. 

## The application structure:   
app.    
├── README.md    
├── __init__.py    
├── __pycache__   
│  ├── __init__.cpython-37.pyc    
│  ├── auth.cpython-37.pyc    
│  ├── main.cpython-37.pyc    
│  └── models.cpython-37.pyc     
├── auth.py    
├── db.sqlite     
├── main.py    
├── models.py    
├── requirements.txt    
├── static    
│  ├── board.css     
│  ├── board.js     
│  ├── icons     
│  │  └── favicon.ico    
│  └── signup.css    
└── templates    
  ├── board.html     
  ├── index.html          
  └── signup.html  

As shown in the diagram above, the webapp has three main python files. First, one is the "__init__.py", which holds the necessary configuration for the Flask web server, and initializes the blueprint for the server ("Authentication" and "The main board"). The second python file, which is "auth.py", is handling the login/signup process for the users and its routes. Finally, the "main.py" is handling all the routes related to the task management process and communicating with the database. The HTML files are stored in the "templates" folder. The static folder is storing all the styling and the javascript files for the frontend.


## Extra features:
Registering a new user
Checking if the same email is existing in the database after signup
Authenticating as a user
Logging out
Maintaining a logged-in session
Switching tasks current status through drag and drop 
Adding form validation in the frontend for checking that the user is going through the baseline for the information 
Encrypting the passwords in the database
Added an extra section for task description (collapsable for saving space)
Responsive frontend page for different desktop sizes.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure to install all the dependencies mentioned in the requirements.txt. Also, running the web app on your local machine requires an internet connection because there are some external libs' CDNs used.

The project requires python3 to be up and running. 

### Installing
- Clone the project on your local machine.
- Go to the project directory.
- Install all the required dependencies for the project.
- Run the following commands in your Mac Terminal to get the server up and running.       
```
$ export FLASK_APP=app      
```
```
$ flask run
```

- After that, click on sign up then create an account. 
- Enjoy!
