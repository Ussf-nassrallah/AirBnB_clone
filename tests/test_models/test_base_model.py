#!/usr/bin/python3
'''
    All the tests for the base_model are contained within this implementation.
'''

from models.base_model import BaseModel
import sys
import unittest
import time
from io import StringIO
import datetime


class TestBaseModel(unittest.TestCase):
    '''
        Testing the BaseModel class.
    '''

    def setUp(self):
        ''' create a new model from the BaseModel '''
        self.new_model = BaseModel()
        self.new_model.name = "youssef nasrallah"

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

    def test_name_value(self):
        ''' change name value '''
        self.new_model.name = "Redwan Ben Yechou"
        self.assertEqual(self.new_model.name, "Redwan Ben Yechou")

    def test_date_time_equal(self):
        ''' checks if created_at equal updated_at '''
        obj = BaseModel()
        # first let's checks new_model date and time
        self.assertEqual(self.new_model.created_at, self.new_model.updated_at)
        # second let's checks our obj
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_save_method(self):
        ''' test save method '''
        last_update = self.new_model.updated_at
        time.sleep(1)
        self.new_model.save()
        self.assertNotEqual(last_update, self.new_model.updated_at)

    def test_str_method(self):
        ''' test __str__ method '''
        copy = sys.stdout
        _id = self.new_model.id
        cap_output = StringIO()
        sys.stdout = cap_output
        print(self.new_model)
        _list = cap_output.getvalue().split(" ")
        self.assertEqual(_list[0], "[BaseModel]")
        self.assertEqual(_list[1], "({})".format(_id))
        sys.stdout = copy

    def test_to_dict_out_type(self):
        ''' test : checks the type of output for to_dict method '''
        obj = {}
        self.assertEqual(type(obj), type(self.new_model.to_dict()))

    def test_to_dict_class_name(self):
        ''' checks class name value in dict '''
        class_name = "BaseModel"
        self.assertEqual(class_name, self.new_model.to_dict()['__class__'])

    def test_to_dict_created_at(self):
        ''' checks created_at type in dict '''
        s = "string"
        self.assertEqual(type(s), type(self.new_model.to_dict()['created_at']))

    def test_to_dict_updated_at(self):
        ''' checks updated_at type in dict '''
        s = "string"
        self.assertEqual(type(s), type(self.new_model.to_dict()['updated_at']))

    def test_kwargs(self):
        ''' test : instances created using kwargs '''
        obj_0 = self.new_model.to_dict()
        obj_1 = BaseModel(**obj_0)
        self.assertEqual(self.new_model.id, obj_1.id)

    def test_created_at_type(self):
        ''' checks the type of created_at '''
        obj_0 = self.new_model.to_dict()
        obj_1 = BaseModel(**obj_0)
        result = isinstance(obj_1.created_at, datetime.datetime)
        self.assertTrue(result)

    def test_updated_at_type(self):
        ''' checks the type of updated_at '''
        obj_0 = self.new_model.to_dict()
        obj_1 = BaseModel(**obj_0)
        result = isinstance(obj_1.updated_at, datetime.datetime)
        self.assertTrue(result)

    def test_dict(self):
        ''' compare two dict '''
        obj_0_dict = self.new_model.to_dict()
        obj_1 = BaseModel(**obj_0_dict)
        obj_1_dict = obj_1.to_dict()
        self.assertEqual(obj_0_dict, obj_1_dict)

    def test_compare_dict(self):
        ''' compare two dict '''
        obj_0_dict = self.new_model.to_dict()
        obj_1 = BaseModel(obj_0_dict)
        self.assertNotEqual(obj_1, self.new_model)
