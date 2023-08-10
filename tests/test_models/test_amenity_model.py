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

    def test_amenity_attributes(self):
        ''' testing amenity class attributes '''
        att = ["name"]
        first_amenity = Amenity()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in first_amenity.__dir__())

    def test_amenity_name_type(self):
        ''' test the type of the name '''
        first_amenity = Amenity()
        # get the name value from the first_Amenity object
        name = getattr(first_amenity, "name")
        # checks the type of the name value
        self.assertIsInstance(name, str)
