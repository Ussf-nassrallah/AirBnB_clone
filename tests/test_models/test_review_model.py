#!/usr/bin/python3
'''
    All the tests for the review_model are
      contained within this implementation.
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

    def test_review_attributes(self):
        ''' testing review class attributes '''
        att = ["place_id", "user_id", "text"]
        first_review = Review()
        for idx in range(0, len(att)):
            self.assertTrue(att[idx] in first_review.__dir__())

    def test_review_place_id_type(self):
        ''' test the type of the place_id '''
        first_review = Review()
        # get the place_id value from the first_review object
        place_id = getattr(first_review, "place_id")
        # checks the type of the place_id value
        self.assertIsInstance(place_id, str)

    def test_review_user_id_type(self):
        ''' test the type of the user_id '''
        first_review = Review()
        # get the user_id value from the first_review object
        user_id = getattr(first_review, "user_id")
        # checks the type of the user_id value
        self.assertIsInstance(user_id, str)

    def test_review_text_type(self):
        ''' test the type of the text '''
        first_review = Review()
        # get the text value from the first_review object
        text = getattr(first_review, "text")
        # checks the type of the text value
        self.assertIsInstance(text, str)
