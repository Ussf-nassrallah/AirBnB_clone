#!/usr/bin/python3
'''
    All the tests for the state_model are contained within this implementation.
'''

from models.state import State
from models.base_model import BaseModel
import unittest


class TestStateModel(unittest.TestCase):
    '''
        Testing state class.
    '''

    def test_state_inherits(self):
        ''' testing State class that inherits from BaseModel '''
        first_state = State()
        self.assertIsInstance(first_state, BaseModel)

    def test_state_attributes(self):
        ''' testing state class attributes '''
        att = ["name"]
        first_state = State()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in first_state.__dir__())

    def test_state_name_type(self):
        ''' test the type of the name '''
        first_state = State()
        # get the name value from the first_state object
        name = getattr(first_state, "name")
        # checks the type of the name value
        self.assertIsInstance(name, str)
