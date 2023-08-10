#!/usr/bin/python3
'''
    All the tests for the city_model are contained within this implementation.
'''

from models.city import City
from models.base_model import BaseModel
import unittest


class TestCityModel(unittest.TestCase):
    '''
        Testing city class.
    '''

    def test_city_inherits(self):
        ''' testing City class that inherits from BaseModel '''
        first_city = City()
        self.assertIsInstance(first_city, BaseModel)
