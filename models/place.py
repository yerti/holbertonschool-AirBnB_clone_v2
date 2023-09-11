#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review


if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                        Column('place_id',
                                String(60),
                                ForeignKey('places.id'),
                                primary_key=True,
                                nullable=False),
                        Column('amenity_id',
                                String(60),
                                ForeignKey('amenities.id'),
                                primary_key=True,
                                nullable=False))


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
        review = 'Review'
        reviews = relationship(review, backref='place', cascade='all, delete')

        amenities = relationship("Amenity", secondary=place_amenity,
                                back_populates="place_amenities",
                                viewonly=False)
    
    ''' relationship with file storage '''
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            ''' Return all reviews '''
            view_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    view_list.append(review)
            return view_list

        @property
        def amenities(self):
            from models.review import Amenity
            amens = storage.all(Amenity)
            list_amens = [amen for amen in amens.values()
                        if amen.id in amenity_ids]
            return list_amens

        @amenities.setter
        def amenities(self, obj):
            if obj.__class__.__name__ == "Amenity":
                amenity_ids.append(obj.id)
            else:
                pass
