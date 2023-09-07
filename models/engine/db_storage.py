#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
import os



class DBStorage:
    """This class manages storage of hbnb models """
    __engine = None
    __session = None

    engine = create_engine(url='mysql+pymysql://{0}\
                :{1}@{2}:{3}/{4}'.format(os.environ['HBNB_MYSQL_USER'],
                    os.environ['HBNB_MYSQL_PWD'],
                    os.environ['HBNB_MYSQL_HOST'], 3306,
                    os.environ['HBNB_MYSQL_DB']), pool_pre_ping=True)

    def __init__(self):
        ''' Create the engine  '''
        self.__engine = engine
    

    def all(self, cls=None):
        """Returns a list of all objects, optionally filtered by class."""
        if cls is None:
            return DBStorage.__objects
        else:
            new_dictionary = {}
            for key, obj in DBStorage.__objects.items():
                if obj.__class__ == cls:
                    new_dictionary[key] = obj
            return new_dictionary

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves database dictionary"""

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review



    def delete(self, obj=None):
        """Remove object from __objects if it exists."""
        if obj is not None:
            new_key = f"{str(obj.__class__.__name__)}.{obj.id}"
