# Capstone Project


# Desing of the Project
The project consists of the two parts: 
    -   Front End.
    -   Back End.


# Models:
Movies with attributes title and release date
Actors with attributes name, age and gender


# Endpoints:
GET /actors and /movies
DELETE /actors/ and /movies/
POST /actors and /movies and
PATCH /actors/ and /movies/


# Roles:
- There are three different roles in the application as described below:
    # Casting Assistant
        Can view actors and movies
    # Casting Director
        All permissions a Casting Assistant has and…
        Add or delete an actor from the database
        Modify actors or movies
    # Executive Producer
        All permissions a Casting Director has and…
        Add or delete a movie from the database


# Tests:
    One test for success behavior of each endpoint
    One test for error behavior of each endpoint
    At least two tests of RBAC for each role

- In order to test the endpoints you have to put the token in test_app.py *****



# Front End
The Front End can be found in the "frontend" folder, and it contains IONIC application. The application has been created only for the purpose of loging in to get the JWT TOKEN, and refresh the token whenever gets expired.


# Back End
The back end can be found under the "starter" folder, and it contains all the Endpoints for the capstone project in addition to the test scripts.


# Getting Started
You need to install the dependencies by going to the `/starter` folder and then run the below command which will install the dependencies.

```bash
pip install -r requirements.txt
```

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```
```bash
export FLASK_ENV=development;
```
To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.



# Heroku:
URL: https://movie-capstone.herokuapp.com/
git: https://git.heroku.com/movie-capstone.git
