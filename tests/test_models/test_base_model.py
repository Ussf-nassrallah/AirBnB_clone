#!/usr/bin/python3
'''
    All the tests for the base_model are contained within this implementation.
'''

from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    '''
        Testing the BaseModel class.
    '''
    def test_obj_type(self):
        ''' test object type '''
        # create some objects from BaseModel for testing
        obj_0 = BaseModel()
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        # Checks that the type of the obj is BaseModel
        self.assertEqual(type(obj_0), BaseModel)
        self.assertEqual(type(obj_1), BaseModel)
        self.assertEqual(type(obj_2), BaseModel)
        # checks that the type of eny objects is BaseModel
        self.assertEqual(type(obj_0), type(obj_1))
        self.assertEqual(type(obj_1), type(obj_2))
        self.assertEqual(type(obj_2), type(obj_0))

    def test_id_type(self):
        ''' test id type '''
        # create some objects from BaseModel for testing
        obj_0 = BaseModel()
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        # Checks that the type of the id is string
        self.assertEqual(type(obj_0.id), type("string"))
        self.assertEqual(type(obj_1.id), type("string"))
        self.assertEqual(type(obj_2.id), type("string"))

    def test_id_values(self):
        ''' test id value '''
        # create some objects from BaseModel for testing
        obj_0 = BaseModel()
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        # checks that eny object has a uniq id
        self.assertNotEqual(obj_0.id, obj_1.id)
        self.assertNotEqual(obj_1.id, obj_2.id)
        self.assertNotEqual(obj_2.id, obj_0.id)
