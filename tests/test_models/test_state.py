#!/usr/bin/python3
""" """
from models.base_model import BaseModel
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """ Cllass that check state module """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
