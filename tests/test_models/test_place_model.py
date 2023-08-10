#!/usr/bin/python3
'''
    All the tests for the place_model are contained within this implementation.
'''

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceModel(unittest.TestCase):
    '''
        Testing place class.
    '''

    def test_place_inherits(self):
        ''' testing Place class that inherits from BaseModel '''
        first_place = Place()
        self.assertIsInstance(first_place, BaseModel)
