#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""

        __tablename__ = "users"

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', backref='user', cascade='all, delete')
        reviews = relationship('Review', backref='user', cascade='all, delete')
else:
    class User(BaseModel):
        email = ""
        password = ""
        first_name = ""
        last_name = ""
