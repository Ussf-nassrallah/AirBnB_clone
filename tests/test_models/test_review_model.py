#!/usr/bin/python3
'''
    All the tests for the review_model are contained within this implementation.
'''

from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReviewModel(unittest.TestCase):
    '''
        Testing review class.
    '''

    def test_review_inherits(self):
        ''' testing Review class that inherits from BaseModel '''
        first_review = Review()
        self.assertIsInstance(first_review, BaseModel)
