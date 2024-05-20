#!/usr/bin/python3
'''class BaseModel that defines all common attributes/methods classes'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''A base class for other models'''
    def __init__(self, *args, **kwargs):
        '''
        Initialize a new instance of BaseModels
        Args:
            *args: list of arguments
            **kwargs: list of key-values arguments
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
            if  'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''Return a string representation of the BaseModels'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''Update the updated_at attribute with the current datetime.'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Return a dictionary containing all keys/values of __dict__'''
        dict_rep = self.__dict__.copy()
        dict_rep['__class__'] = self.__class__.__name__
        dict_rep['created_at'] = self.created_at.isoformat()
        dict_rep['updated_at'] = self.updated_at.isoformat()
        return dict_rep
