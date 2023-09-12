#!/usr/bin/python3
'''
    Test Case for the console
'''
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from console import HBNBCommand
import models


class TestConsole(unittest.TestCase):
    ''' Unittests to test the console '''

    @unittest.skipUnless(models.storage_type == 'db', 'Use with db storage')
    def test_emptyline(self):
        ''' Test empty line '''
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNB.onecmd("\n")
            self.assertEqual('', f.getvalue())

    @unittest.skipUnless(models.storage_type == 'db', 'Use with db storage')
    def test_quit(self):
        """Test quit command """
        with patch("sys.stdout", new=StringIO()) as f:
            self.HBNB.onecmd("quit")
            self.assertEqual('', f.getvalue())


if __name__ == '__main__':
    unittest.main()
