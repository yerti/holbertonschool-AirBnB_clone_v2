#!/usr/bin/python3
""" Module to  test the amenity file """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ Class to test amenity """

    def __init__(self, *args, **kwargs):
        """ The constructor of the class """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Method to test the name """
        new = self.value()
        self.assertEqual(type(new.name), str)
