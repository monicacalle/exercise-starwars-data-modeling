import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(250), unique=True)
    email = Column(String(250)) 
    user_fav = Column(Integer, ForeignKey('favorites.id'), primary_key=True)
    
   
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer,primary_key=True)


class Characters(Base):
    __tablename__ = 'characters'    
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))    
    user_id = Column(Integer, ForeignKey('favorites.id'), primary_key=True)
    
class Planets(Base):
    __tablename__ = 'planets'    
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    user_id = Column(Integer, ForeignKey('favorites.id'), primary_key=True)
    

class vehicles(Base):
    __tablename__ = 'vehicles'    
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    user_id = Column(Integer, ForeignKey('favorites.id'), primary_key=True)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')