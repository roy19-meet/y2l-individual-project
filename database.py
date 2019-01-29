from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
      pass


def create_users(password,username):
  user_object = User(password=password,username=username)
  session.add(user_object)
  session.commit()

def query_by_username(username):
  user_object= session.query(User).filter_by(username=username).first()
  return user_object 


def create_artists(genree,name,neforma,hits):
  artist_object = Artist(genree=genree,name=name,neforma=neforma,hits=hits)
  session.add(artist_object)
  session.commit()

def get_all_artists():
  all_artists = session.query(Artist).all()
  return all_artists

def query_genre(the_genre):
  artists_objects = session.query(Artist).filter_by(genree=the_genre)
  return artists_objects

def query_id(the_id):
  artists_objects=session.query(Artist).filter_by(id=the_id).all()
  return [artist.id for artist in artists_objects]

def give_me_the_hits(the_hits):
  artists_objects=session.query(Artist).filter_by(hits=the_hits).all()
  return [artist.hits for artist in artists_objects]


# def add_like(the_id):
#   to_like= session.query(Artist).filter_by(the_id=the_id).first()
#   to_like.like =to_like.like+1  






  