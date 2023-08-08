#!/usr/bin/python3
'''
    This module contains the definition of the BaseModel class
'''

import uuid
import datetime
import models


class BaseModel:
    '''
        class BaseModel that defines all common attributes/methods
            for other classes
    '''

    def __init__(self, *args, **kwargs):
        ''' Public instance attributes '''
        if (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            kwargs['created_at'] = datetime.datetime.strptime(
                kwargs['created_at'],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
            kwargs['updated_at'] = datetime.datetime.strptime(
                kwargs['updated_at'],
                "%Y-%m-%dT%H:%M:%S.%f"
            )
        else:
            # create a unique id for each BaseModel
            self.id = str(uuid.uuid4())
            # the current datetime when an instance is created
            self.created_at = datetime.datetime.now()
            # the current datetime when an instance is updated
            self.updated_at = datetime.datetime.now()
            # link BaseModel to FileStorage by using the variable storage
            models.storage.new(self)

    def save(self):
        '''
            updates the public instance attribute updated_at
                with the current datetime
        '''
        self.updated_at = datetime.datetime.now()
        # call save
        models.storage.save()

    def __str__(self):
        '''
            Return a string that representation of BaseModel class
        '''
        s = "[{}] ({}) {}"
        return s.format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        '''
            returns a dictionary containing all keys/values of __dict__ of the instance
        '''
        dct = dict(self.__dict__)
        dct['__class__'] = type(self).__name__
        dct['created_at'] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dct['updated_at'] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dct
