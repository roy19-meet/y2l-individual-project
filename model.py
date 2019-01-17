from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Artist(Base):
	 __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    Genre= Column(String)
    Name = Column(String)
    Info = Column(String)
    Hits= Column(String)
    

    pass
