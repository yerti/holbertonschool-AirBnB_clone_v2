#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        __tablename__ = 'amenities'

        name = Column(String(128), nullable=False)
        relation = relationship
        plac = 'Place'
        p_a = 'place_amenity'
        ament = "amenities"
        place_amenities = relation(plac, secondary=p_a, back_populates=ament)
else:
    class Amenity(BaseModel):
        """We create public attributes"""
        name = ""
