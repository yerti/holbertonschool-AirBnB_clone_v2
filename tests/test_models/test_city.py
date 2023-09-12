#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)


if __name__ == '__main__':
    unittest.main()
