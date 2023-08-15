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

    def test_user_attributes(self):
        ''' testing User class attributes '''
        att = ["email", "password", "first_name", "last_name"]
        first_user = User()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in first_user.__dir__())

    def test_user_fname_type(self):
        ''' test the type of user first_name '''
        first_user = User()
        # get first_name value from first_user object
        first_name = getattr(first_user, "first_name")
        # checks the type of first_name value
        self.assertIsInstance(first_name, str)

    def test_user_lname_type(self):
        ''' test the type of user last_name '''
        first_user = User()
        # get last_name value from first_user object
        last_name = getattr(first_user, "last_name")
        # checks the type of last_name value
        self.assertIsInstance(last_name, str)

    def test_user_email_type(self):
        ''' test the type of user email '''
        first_user = User()
        # get email value from first_user object
        email = getattr(first_user, "email")
        # checks the type of email value
        self.assertIsInstance(email, str)

    def test_user_password_type(self):
        ''' test the type of user password '''
        first_user = User()
        # get password value from first_user object
        password = getattr(first_user, "password")
        # checks the type of password value
        self.assertIsInstance(password, str)
