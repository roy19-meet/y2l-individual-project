from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Artist(Base):
  __tablename__ = 'artists1'
  id = Column(Integer, primary_key=True)
  genree = Column(String)
  name = Column(String)
  neforma = Column(String)
  hits = Column(String)




class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  password = Column(String)
  username = Column(String)
 



    

  pass
