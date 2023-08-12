#!/usr/bin/python3
'''
  model that contains a FileStorage class that
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
import json
import os


class FileStorage:
    ''' Represents the FileStorage class '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' Sets in __objects the new obj '''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to the JSON file '''
        filename = self.__file_path
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(filename, 'w') as file:
            json.dump(data, file)

    def reload(self):
        ''' Deserializes the JSON file to __objects '''
        filename = self.__file_path
        self.__objects = {}
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except Exception as e:
            return
        for key, value in data.items():
            class_name, obj_id = key.split('.')
            if class_name == 'BaseModel':
                self.__objects[key] = BaseModel(**value)
            elif class_name == 'User':
                self.__objects[key] = User(**value)
            elif class_name == 'State':
                self.__objects[key] = State(**value)
            elif class_name == 'City':
                self.__objects[key] = City(**value)
            elif class_name == 'Review':
                self.__objects[key] = Review(**value)
            elif class_name == 'Amenity':
                self.__objects[key] = Amenity(**value)
            elif class_name == 'Place':
                self.__objects[key] = Place(**value)
