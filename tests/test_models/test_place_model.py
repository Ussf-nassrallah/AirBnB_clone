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

    def test_place_attributes(self):
        ''' testing place class attributes '''
        att = [
            "city_id",
            "user_id",
            "name",
            "description",
            "number_rooms",
            "number_bathrooms",
            "max_guest",
            "price_by_night",
            "latitude",
            "longitude",
            "amenity_ids"
        ]
        first_place = Place()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in first_place.__dir__())

    def test_place_cityId_type(self):
        ''' test the type of the cityId '''
        first_place = Place()
        # get the cityId value from the first_place object
        city_id = getattr(first_place, "city_id")
        # checks the type of city_id value
        self.assertIsInstance(city_id, str)

    def test_place_userId_type(self):
        ''' test the type of the userId '''
        first_place = Place()
        # get the user_id value from the first_place object
        user_id = getattr(first_place, "user_id")
        # checks the type of user_id value
        self.assertIsInstance(user_id, str)

    def test_place_name_type(self):
        ''' test the type of the name '''
        first_place = Place()
        # get the name value from the first_place object
        name = getattr(first_place, "name")
        # checks the type of name value
        self.assertIsInstance(name, str)

    def test_place_desc_type(self):
        ''' test the type of the description '''
        first_place = Place()
        # get the description value from the first_place object
        description = getattr(first_place, "description")
        # checks the type of the description value
        self.assertIsInstance(description, str)

    def test_place_nr_type(self):
        ''' test the type of the number_rooms '''
        first_place = Place()
        # get the number_rooms value from the first_place object
        number_rooms = getattr(first_place, "number_rooms")
        # checks the type of the number_rooms value
        self.assertIsInstance(number_rooms, int)

    def test_place_nb_type(self):
        ''' test the type of the number_bathrooms '''
        first_place = Place()
        # get the number_bathrooms value from the first_place object
        number_bathrooms = getattr(first_place, "number_bathrooms")
        # checks the type of the number_bathrooms value
        self.assertIsInstance(number_bathrooms, int)

    def test_place_mg_type(self):
        ''' test the type of the max_guest '''
        first_place = Place()
        # get the max_guest value from the first_place object
        max_guest = getattr(first_place, "max_guest")
        # checks the type of the max_guest value
        self.assertIsInstance(max_guest, int)

    def test_place_pbn_type(self):
        ''' test the type of the price_by_night '''
        first_place = Place()
        # get the price_by_night value from the first_place object
        price_by_night = getattr(first_place, "price_by_night")
        # checks the type of the price_by_night value
        self.assertIsInstance(price_by_night, int)

    def test_place_latitude_type(self):
        ''' test the type of the latitude '''
        first_place = Place()
        # get the latitude value from the first_place object
        latitude = getattr(first_place, "latitude")
        # checks the type of the latitude value
        self.assertIsInstance(latitude, float)

    def test_place_longitude_type(self):
        ''' test the type of the longitude '''
        first_place = Place()
        # get the longitude value from the first_place object
        longitude = getattr(first_place, "longitude")
        # checks the type of the longitude value
        self.assertIsInstance(longitude, float)

    def test_place_amenity_ids_type(self):
        ''' test the type of the amenity_ids '''
        first_place = Place()
        # get the amenity_ids value from the first_place object
        amenity_ids = getattr(first_place, "amenity_ids")
        # checks the type of the amenity_ids value
        self.assertIsInstance(amenity_ids, list)