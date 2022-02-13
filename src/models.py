import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(250), unique=True)
    email = Column(String(250), unique=True)       
   
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)

class Characters(Base):
    __tablename__ = 'characters'    
    id = Column(Integer,primary_key=True)
    name = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))   
    
class Planets(Base):
    __tablename__ = 'planets'    
    id = Column(Integer,primary_key=True)
    name = Column(String(250))    

class Vehicles(Base):
    __tablename__ = 'vehicles'    
    id = Column(Integer,primary_key=True)
    name = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')