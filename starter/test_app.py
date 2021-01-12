import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask import request

from app import create_app
from models import setup_db, Movie, Actor
# Added
import http.client
from jose import jwt
from auth import verify_decode_jwt


class MovieTestCase(unittest.TestCase):
    """This class represents the movie test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "movie_test"
        self.database_path = "postgres://{}/{}".format('postgres:13245@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)


        # Need to update the token when it is expired in order for the test cases to work
        # Note that for each role, you need to put the proper token to test RBAC
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1wME4yMnFHQkNnQVRkdXRRU0MzeSJ9.eyJpc3MiOiJodHRwczovL2NoZWNrLWxvZ2luLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmZkMzRlMjQyNTJhOTAwNmZiNmQ5MWMiLCJhdWQiOiJNb3ZpZSIsImlhdCI6MTYxMDQ2MTY0NiwiZXhwIjoxNjEwNDY4ODQ2LCJhenAiOiJ6WmNuQVdLSGJQelRPYUx3ckdiOEpwSkcybUNsWnI0RyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.YU5ED9cVqLOJwXRYdsFu0Sae3VvcF0hjQSZOhFTwbrqERUZODzRWswiYQmfZzHihEAESdK6JKRe2aRIk9qDUliX1Wd8_gYusql56Q_ll7BzbmMu2uhGtb_0G47xYhpl3HzjF80XbuBbwiahtMP4M8AsAtVKmyc9wkJVjn4DJ-jnEbFsuI-u0phP_GS1eALmpQrgyXef7-X7giwgiMMkJcUt8B_f-HWV-A3fxQdPqeHHRdQxsdYl9fRrkyjX-poRBWutpe0QnBow1nofefj7GML5eDm_AWYay5_J1IzgpDQnetUKHll_3tKns55xy0TBYBeP8axZ-IbtpweVSplXr2A'
        }

        self.movie = {
            "title": "Hitman",
            "releaseDate": "09-April-1998"
        }

        self.movie_with_no_title = {
            "title": "",
            "releaseDate": "09-April-1998"
        }

        self.new_movie = {
            "title": "New Hitman Movie",
            "releaseDate": "09-April-2019"
        }

        self.actor = {
            "name": "Mohammed",
            "age": 56,
            "gender": "M"
        }

        self.actor_with_no_name = {
            "name": "",
            "age": 56,
            "gender": "M"
        }


        self.new_actor = {
            "name": "Khaled",
            "age": 23,
            "gender": "M"
        }
    
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()


    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    # 1) Test Cases for /movies
    def test_Getting_All_Movies(self):
        # self.headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1wME4yMnFHQkNnQVRkdXRRU0MzeSJ9.eyJpc3MiOiJodHRwczovL2NoZWNrLWxvZ2luLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZmFhYjFkYTlhYjJkMDAwNzZmNDhhODAiLCJhdWQiOiJNb3ZpZSIsImlhdCI6MTYwOTk1NTk3NSwiZXhwIjoxNjA5OTYzMTc1LCJhenAiOiJ6WmNuQVdLSGJQelRPYUx3ckdiOEpwSkcybUNsWnI0RyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSIsInB1dDphY3RvciIsInB1dDptb3ZpZSJdfQ.eySh_SusGrOwgv2Gi6-X3n6rB-PS4NmhzT7rc2wWLctui9A7gKab61mOsUqFXMUfXg7IZEnP9nZdta4M13wUnqzONDGbyEIJlT1wc8G0jmjXk9AYD--muLlO1nWRyFoJ3vsxzwgytpEDXh0VGoMQ7IJ7tdf1sGHXIGNdJhesqzO8THRY_tds5Otz7c9J5iNSaynaAuVyifviCw8wcZMNDaNoTzwdSSpHMvtrl4897qbcD7KR6pz-Pyd-wnhi8rL0zqbZhKXLmFarUlWPw-X_DxFn3KlHuNI1NxtPy8tIbl_0VTdBqMX1mRCgMJyYaZ32kPq1Hqew7C9CZ63R21cDGQ'}
        res = self.client().get('/movies', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)


    def test_delete_movie(self):
        res = self.client().delete('/movies/1', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_movie(self):
        res = self.client().post('/movies', headers = self.headers, json = self.movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_movie(self):
        res = self.client().patch('/movies/3', headers = self.headers, json = self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # Test Cases for Error behavior for Movie    ### ERROR CASES ###

    # Get - You need to empty the movie table in order for this case to work
    def test_error_get_movies(self):
        res = self.client().get('/movies', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)

    # Delete
    def test_error_delete_movie(self):
        res = self.client().delete('/movies/1000', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)

    # Post
    def test_error_post_movie(self):
        res = self.client().post('/movies', headers = self.headers, json = self.movie_with_no_title)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)

    # Patch
    def test_error_update_movie(self):
        res = self.client().patch('/movies/1000', headers = self.headers, json = self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)



    # 2) Test Cases for /actors
    def test_Getting_All_Actors(self):
        res = self.client().get('/actors', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)


    def test_delete_actor(self):
        res = self.client().delete('/actors/1', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_post_actor(self):
        res = self.client().post('/actors', headers = self.headers, json = self.actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_actor(self):
        res = self.client().patch('/actors/3', headers = self.headers, json = self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)



    # Test Cases for ERROR for Actors
        # Get You need to empty the actor table in order for this case to work
    def test_error_get_actors(self):
        res = self.client().get('/actors', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)

    # Delete
    def test_error_delete_actor(self):
        res = self.client().delete('/actors/1000', headers = self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)

    # Post
    def test_error_post_actor(self):
        res = self.client().post('/actors', headers = self.headers, json = self.actor_with_no_name)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)

    # Patch
    def test_error_update_actor(self):
        res = self.client().patch('/actors/1000', headers = self.headers, json = self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(data['success'], False)




    # 3) RBAC Test Cases for Each Role

    # Casting Assistant Role:
    def test_casting_assistant_with_delete_movie_role(self):
        res = self.client().delete('/movies/1', headers = self.headers)
        # data = json.loads(res.data)

        header = self.headers
        token_header = header['Authorization']
        token = token_header.split(' ')[1]
 
        payload = verify_decode_jwt(token)
        permissions = payload['permissions']
        print(permissions)
        
        if 'delete:movie' not in permissions:
            no_permission = False

        self.assertEqual(no_permission, False)


    def test_casting_assistant_with_psot_movie_role(self):
        res = self.client().post('/movies', headers = self.headers, json = self.new_movie)
        # data = json.loads(res.data)

        header = self.headers
        token_header = header['Authorization']
        token = token_header.split(' ')[1]
 
        payload = verify_decode_jwt(token)
        permissions = payload['permissions']
        print(permissions)
        
        if 'post:movie' not in permissions:
            no_permission = False

        self.assertEqual(no_permission, False)

              

    # Casting Director Role:

    def test_casting_director_with_delete_movie_role(self):
        res = self.client().delete('/movies/1', headers = self.headers)

        header = self.headers
        token_header = header['Authorization']
        token = token_header.split(' ')[1]
 
        payload = verify_decode_jwt(token)
        permissions = payload['permissions']
        print(permissions)
        
        if 'delete:movie' not in permissions:
            no_permission = False

        self.assertEqual(no_permission, False)


    def test_casting_director_with_psot_movie_role(self):
        res = self.client().post('/movies', headers = self.headers, json = self.new_movie)

        header = self.headers
        token_header = header['Authorization']
        token = token_header.split(' ')[1]
 
        payload = verify_decode_jwt(token)
        permissions = payload['permissions']
        print(permissions)
        
        if 'post:movie' not in permissions:
            no_permission = False

        self.assertEqual(no_permission, False)



    # Executive Producer Role:

    def test_executive_producer_with_delete_movie_role(self):
        res = self.client().delete('/movies/1', headers = self.headers)

        header = self.headers
        token_header = header['Authorization']
        token = token_header.split(' ')[1]
 
        payload = verify_decode_jwt(token)
        permissions = payload['permissions']
        
        if 'delete:movie' in permissions:
            permission = True

            self.assertEqual(permission, True)


    def test_executive_producer_with_psot_movie_role(self):
        res = self.client().post('/movies', headers = self.headers, json = self.new_movie)

        header = self.headers
        token_header = header['Authorization']
        token = token_header.split(' ')[1]
 
        payload = verify_decode_jwt(token)
        permissions = payload['permissions']
        
        if 'post:movie' in permissions:
            permission = True

            self.assertEqual(permission, True)




# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()