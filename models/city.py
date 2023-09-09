#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel,Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        place = relationship('Place', backref='cities')
    else:
        name = ''
        state_id = ''
