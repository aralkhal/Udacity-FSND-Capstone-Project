# Capstone Project


# Motivation 
This project is one of the most important projects in the Nano-Degree since it combines most of the 
topics we have learned during the Nano-Degree. In addition, we have gained a new experienvce by dealing or deploying our application live via Heroku.


# Desing of the Project
The project consists of the two parts: 
    -   Front End.
    -   Back End.


# Database Models:
- Movies with attributes title and release date as shown below: 
    class Movie(db.Model):  
        __tablename__ = 'movies'

        id = Column(Integer, primary_key=True)
        title = Column(String)
        releaseDate = Column(String)

- Actors with attributes name, age and gender, as shown below: 
    class Actor(db.Model):
        __tablename__ = "actors"

        id = Column(Integer, primary_key=True)
        name = Column(String)
        age = Column(Integer)
        gender = Column(String)


# Endpoints:
Below are the Endpoints with the expected return value in JSON format: 

1) GET /movies
{
    "movies": [
        {
            "id": 1,
            "release_Date": "09-April-2019",
            "title": "Hitman Movie"
        },
        {
            "id": 2,
            "release_Date": "10-June-1990",
            "title": "Titanic"
        },
        {
            "id": 3,
            "release_Date": "20-May-1995",
            "title": "The End"
        },
        {
            "id": 4,
            "release_Date": "20-August-1999",
            "title": "Harry Potter"
        },
        {
            "id": 5,
            "release_Date": "03-January-1988",
            "title": "The Lion King"
        }
    ],
    "success": true
}

2) DELETE /movies/{id}
return {
            'success': True
        }

3) POST /movies
return {
            'success': True
        }

4) PATCH /movies/{id}
return {
            'success': True
        }

5) GET /actors
Return the below:
{
    "actors": [
        {
            "age": 56,
            "gender": "M",
            "id": 1,
            "name": "John"
        },
        {
            "age": 30,
            "gender": "M",
            "id": 2,
            "name": "Abdullah"
        },
        {
            "age": 37,
            "gender": "M",
            "id": 3,
            "name": "Mohammed"
        },
        {
            "age": 42,
            "gender": "M",
            "id": 4,
            "name": "Mike"
        },
        {
            "age": 23,
            "gender": "F",
            "id": 5,
            "name": "Sarah"
        },
        {
            "age": 29,
            "gender": "F",
            "id": 6,
            "name": "Nawal"
        }
    ],
    "success": true
}

6) DELETE /actors/{id}
return {
            'success': True
        }


7) POST /actors
return  {
            'success': False
        }

8) PATCH /actors/{id}
return {
                'success': False
            }


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




# Front End  ( THIS PART HAS BEEN REMOVED )
The Front End can be found in the "frontend" folder, and it contains IONIC application. The application has been created only for the purpose of loging in to get the JWT TOKEN, and refresh the token whenever gets expired.


# Back End
The back end can be found under the "starter" folder, and it contains all the Endpoints for the capstone project in addition to the test scripts.


# Getting Started (Using Virtual Environment)
You need to install the dependencies by going to the `/starter` folder and then run the below command which will install the dependencies.

```bash
pip3 install -r requirements.txt
```

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

# ON Linux:
```bash
export FLASK_APP=app.py;
```
```bash
export FLASK_ENV=development;
```
To run the server, execute:

```bash
flask run --reload
```

# On Windows
set FLASK_APP=app.py

set FLASK_ENV=development

flask run


The `--reload` flag will detect file changes and restart the server automatically.



# Heroku:
URL: https://new-movie-capstone-api.herokuapp.com/
git: https://git.heroku.com/new-movie-capstone-api.git
