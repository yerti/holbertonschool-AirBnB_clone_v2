#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import MetaData, create_engine
import os
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages databases of hbnb models """
    __engine = None
    __session = None


    def __init__(self):
        ''' Connect the motor of the database '''
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        
        self.__engine = create_engine(url='mysql+mysqldb://{0}:{1}@{2}/{3}'.
                format(user, password, host, database),pool_pre_ping=True)

        if user == 'test':
            ''' Drop all tables if variable HBNB_ENV is equal to test '''
            Base.metadata.drop_all(self.__engine)
        
    def all(self, cls=None):
        """Returns a list of objects, optionally filtered by class."""
        db = {}
        all_classes = ['User', 'Review', 'Place', 'City', 'State']
        if cls is None:
            for cl in self.all_classes:
                cl = eval(cl)
                for instance in self.__session.query(cl).all():
                    key = instance.__class__.__name__ + '.' + instance.id
                    db[key] = instance
        else:
            for instance in self.__session.query(cls).all():
                key = instance.__class__.__name__ + '.' + instance.id
                db[key] = instance
        return db

    def new(self, obj):
        """Adds new object to dbstorage dictionary"""
        self.__session.add(obj)
    
    def save(self):
        """Saves database dictionary"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        
        Base.metadata.create_all(self.__engine)
        session_db = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_db)
        self.__session = Session()

    def delete(self, obj=None):
        """Remove object from __objects if it exists."""
        if obj is not None:
           self.__sesion.delete(obj) 
