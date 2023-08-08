#!/usr/bin/python3
'''
  model thats contain a FileStorage class that
    serializes instances to a JSON file and
    deserializes JSON file to instances
'''
import json
import os

class FileStorage:
    ''' represent FileStorage class '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' function thats returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the new obj '''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file '''
        with open(self.__file_path, 'a') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        ''' deserializes the JSON file to __objects '''
        if os.path.exists(self.__file_path):
            json.loads(self.__objects)
