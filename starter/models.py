from sqlalchemy import Column, String, create_engine, Integer
from flask_sqlalchemy import SQLAlchemy
import json

# ENV = 'dev'

# if ENV == 'dev':
#   # app.debug = True
#   database_name = "movie"
#   database_path = "postgres://{}/{}".format('postgres:13245@localhost:5432', database_name)
# else:
#   # Production
#   # app.debug = False
#   database_name = "movie"
#   database_path = "postgres://{}/{}".format('postgres:13245@localhost:5432', database_name)

# database_path = os.environ['DATABASE_URL']

database_name = "movie"
# Dev or locally - need to uncomment the below to run locally: 
# database_path = "postgres://{}/{}".format('postgres:13245@localhost:5432', database_name)

# This the Heroku Postgres Database:
database_path = 'postgres://djabbjxegwdzls:ec1a2636b48c8226f7a45997401928a6060403096893cb54981394f926a98f98@ec2-18-213-176-229.compute-1.amazonaws.com:5432/d77cfo6rubivgk'


db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()


'''
Movie Table with 
Have title and release year
'''
class Movie(db.Model):  
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  releaseDate = Column(String)

  def __init__(self, title, releaseDate):
    self.title = title
    self.releaseDate = releaseDate

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_Date': self.releaseDate
    }


# Actors Table 
class Actor(db.Model):
  __tablename__ = "actors"

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def update(self):
    db.session.commit()

  def format(self):
    return {
      "id": self.id,
      "name": self.name,
      "age": self.age,
      "gender": self.gender
    }
