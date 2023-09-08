#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import os
from models.base_model import BaseModel


Base = declarative_base()
metadata = MetaData()


class DBStorage:
    """This class manages databases of hbnb models """
    __engine = None
    __session = None

    user = os.getenv('HBNB_MYSQL_USER')
    password = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    database = os.getenv('HBNB_MYSQL_DB')

    def __init__(self):
        ''' Connect the file to the database '''
        self.__engine = create_engine(url='mysql+mysqldb://{0}:{1}@{2}:{3}/{4}'.
                format(self.user, self.password, self.host, 3306,self.database),
                pool_pre_ping=True)
        
        Session = sessionmaker(bind=self.__engine)
        session = Session()

        if os.getenv('HBNB_ENV') == 'test':
            ''' Drop all tables if variable HBNB_ENV is equal to test '''
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

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
        self.session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        
        Base.metadata.create_all(self.__engine) 


    def delete(self, obj=None):
        """Remove object from __objects if it exists."""
        if obj is not None:
            self.__session.delete(obj)
