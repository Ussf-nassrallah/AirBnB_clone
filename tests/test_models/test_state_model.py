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
