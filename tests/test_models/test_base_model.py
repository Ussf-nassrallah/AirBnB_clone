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
        obj = BaseModel()
        self.assertEqual(type(obj), type(BaseModel))