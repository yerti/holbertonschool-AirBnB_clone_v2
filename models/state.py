#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("city", backref="state", cascade="all, delete")
    else:
        name = ""

    """function that calculates and returns all cities related to this intanica"""
    """The property decorator only allows access to the function as if it were just a read attribute."""
    @property
        def cities(self):
            new_list_cities = []
            for city in models.storage.all('City').values():
                if city.state_id == self.id:
                    new_list_cities.append(city)

            return new_list_cities
