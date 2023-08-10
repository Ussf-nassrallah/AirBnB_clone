#!/usr/bin/python3
'''
    All the tests for the user_model are contained within this implementation.
'''

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUserModel(unittest.TestCase):
    '''
        Testing User class.
    '''

    def test_user_inherits(self):
        ''' testing User class that inherits from BaseModel '''
        first_user = User()
        self.assertIsInstance(first_user, BaseModel)
