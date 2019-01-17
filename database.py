from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def function(parameter):
      pass
    

def create_artists(Genre,Name,Info,Hits):
	artist_object = Artist(Genre=Genre,Name=Name,Info=Info,Hits=Hits)
    session.add(artist_object)
    session.commit()

def get_all_artists():
  all_artists = session.query(Artist).all()
  return all_artists

def get_rock_artists():
  rock_artists = session.query(Artist).filter_by(Genre=the_genre)
  return rock_artists







  