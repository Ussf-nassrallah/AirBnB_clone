#!/usr/bin/python3
'''
    testing: model thats contain a FileStorage class that
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    ''' represent TestFileStorage class '''
    def setUp(self):
        '''
            init classes:
                store from FileStorage
                obj from BaseModel
        '''
        self.store = FileStorage()
        self.obj = BaseModel()

    def tearDown(self):
        ''' remove (file.json) after testing '''
        filename = 'file.json'
        try:
            os.remove(filename)
        except FileNotFoundError:
            pass

    def test_setup(self):
        ''' checks if store and obj classes are presents '''
        _store = self.store
        _obj = self.obj
        self.assertIsInstance(_store, FileStorage)
        self.assertIsInstance(_obj, BaseModel)

    def test_objects_type(self):
        ''' checks the type of __objects -> should be a dict '''
        _store = self.store
        # you can't access to __objects because it's private attribute
        # thats why, I will use all() method to checks the return value
        self.assertIsInstance(_store.all(), dict)

    def test_all_method(self):
        ''' test: all() method '''
        _store = self.store
        new_store = FileStorage()
        self.assertIsInstance(_store.all(), dict)
        self.assertIsInstance(new_store.all(), dict)
        self.assertEqual(type(_store.all()), type(new_store.all()))

    def test_new_method(self):
        ''' test: new() method '''
        _store = self.store
        # create 2 objects from BaseModel for testing
        _obj = self.obj
        new_obj = BaseModel()
        # store objects
        _store.new(_obj)
        _store.new(new_obj)
        # checks the len of __objects dict
        # self.assertEqual(len(_store.all()), 2)
        # checks the key for each obj in __objects
        _obj_k = f"{_obj.__class__.__name__}.{_obj.id}"
        new_obj_k = f"{new_obj.__class__.__name__}.{new_obj.id}"
        self.assertTrue(_obj_k in _store.all())
        self.assertTrue(new_obj_k in _store.all())

    def test_save_method(self):
        ''' test: save() method '''
        # checks file exists
        filename = "file.json"
        _store = self.store
        _store.save()
        self.assertTrue(os.path.isfile(filename))

    def test_file_reading(self):
        ''' checks file data '''
        filename = "file.json"
        _obj = self.obj
        _store = self.store
        _store.save()
        _store.new(_obj)

        with open(filename, 'r') as file:
            data = json.load(file)
        self.assertTrue(type(data) is dict)

    def test_file_data_type(self):
        ''' checks the data type in file.json '''
        filename = "file.json"
        _obj = self.obj
        _store = self.store
        _store.save()
        _store.new(_obj)

        with open(filename, 'r') as file:
            data = file.read()
        self.assertIsInstance(data, str)

    def test_reload_method(self):
        ''' test reload method if file.json not exists '''
        try:
            _store = self.store
            _store.reload()
            self.assertTrue(True)
        except:
            self.assertTrue(False)