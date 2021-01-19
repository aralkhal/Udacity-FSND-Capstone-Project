import os
from flask import Flask, jsonify, abort, json, request
from models import setup_db, Movie, Actor
# Added
from flask_cors import CORS
# from auth.auth import AuthError, requires_auth
from auth import AuthError, requires_auth

 
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)
 
    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        if excited == 'true':
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    # End Point to get all the movies
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies():

        movies = Movie.query.all()

        if movies is None:
            return jsonify({
                'success': False
            })

        if len(movies) == 0:
            abort(422)

        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        })

    # EndPoint to delete a movie
    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(id):
        movie = Movie.query.filter(Movie.id == id).one_or_none()

        print("Hello from Delete ")

        if movie is None:
            abort(422)

        Movie.delete(movie)

        return jsonify({
            'success': True
        })

    # EndPoint to add/post a movie
    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def add_movie():
        body = request.get_json()

        movie_title = body.get('title', None)
        movie_released_date = body.get('releaseDate', None)

        # print('Movie_title  ====  ', movie_title)
        if movie_title == "":
            return jsonify({
                'success': False
            })

        movie = Movie(title=movie_title, releaseDate=movie_released_date)

        Movie.insert(movie)

        return jsonify({
            'success': True
        })

    # EndPoint to update a movie

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('put:movie')
    def update_movie(id):
        body = request.get_json()
        new_movie_title = body.get('title', None)
        new_movie_released_date = body.get('releaseDate', None)

        movie = Movie.query.filter(Movie.id == id).one_or_none()

        if movie is None:
            return jsonify({
                'success': False
            })

        movie.title = new_movie_title
        movie.releaseDate = new_movie_released_date

        Movie.update(movie)

        return jsonify({
            'success': True
        })

    # End Point to get all actors

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors():
        # get actors from DB
        actors = Actor.query.all()

        if actors is None:
            return jsonify({
                'success': False
            })

        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        })

    # EndPoint to delete an actor
    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(id):
        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            abort(422)

        Actor.delete(actor)

        return jsonify({
            'success': True
        })

    # EndPoint to add/post a actor

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def add_actor():
        body = request.get_json()

        actor_name = body.get('name', None)
        actor_age = body.get('age', None)
        actor_gender = body.get('gender', None)

        if actor_name == "":
            return jsonify({
                'success': False
            })

        actor = Actor(name=actor_name, age=actor_age, gender=actor_gender)

        Actor.insert(actor)

        return jsonify({
            'success': True
        })

    # EndPoint to update a actor

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('put:actor')
    def update_actor(id):
        body = request.get_json()
        new_actor_name = body.get('name', None)
        new_actor_age = body.get('age', None)
        new_actor_gender = body.get('gender', None)

        actor = Actor.query.filter(Actor.id == id).one_or_none()

        if actor is None:
            return jsonify({
                'success': False
            })

        actor.name = new_actor_name
        actor.age = new_actor_age
        actor.gender = new_actor_gender

        Actor.update(actor)

        return jsonify({
            'success': True
        })

    @app.errorhandler(422)
    def cannot_be_processed(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'The request cannot be processed'
        }), 422

    @app.errorhandler(403)
    def forbidden_access(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'Forbidden Access'
        }), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'Page not Found'
        }), 404

    @app.errorhandler(401)
    def unauthorized_action(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'unauthorized action'
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
