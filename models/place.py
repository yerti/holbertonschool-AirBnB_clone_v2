#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.review import Review

class Place(BaseModel, Base):

    __tablename__ = 'places'

    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place', cascade='all, delete')
    else:
        ''' relationship with file storage '''
        @property
        def reviews(self):
            ''' Return all reviews '''
            view_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    view_list.append(review)
            return view_list

