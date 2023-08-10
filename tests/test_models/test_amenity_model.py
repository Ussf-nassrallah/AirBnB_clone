#!/usr/bin/python3
'''
    All the tests for the amenity_model are contained within this implementation.
'''

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenityModel(unittest.TestCase):
    '''
        Testing Amenity class.
    '''

    def test_amenity_inherits(self):
        ''' testing Amenity class that inherits from BaseModel '''
        first_amenity = Amenity()
        self.assertIsInstance(first_amenity, BaseModel)
