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

    def test_city_attributes(self):
        ''' testing city class attributes '''
        att = ["state_id", "name"]
        first_city = City()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in first_city.__dir__())

    def test_city_state_id_type(self):
        ''' test the type of the state_id '''
        first_city = City()
        # get the state_id value from the first_city object
        state_id = getattr(first_city, "state_id")
        # checks the type of the state_id value
        self.assertIsInstance(state_id, str)

    def test_city_name_type(self):
        ''' test the type of the name '''
        first_city = City()
        # get the name value from the first_city object
        name = getattr(first_city, "name")
        # checks the type of the name value
        self.assertIsInstance(name, str)
