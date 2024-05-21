#!/usr/bin/python3
"""
Serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    '''Serializes instances to a JSON file and deserializes file to instances.'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return type(self).__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj.id in type(self).__objects:
            print("exists")
            return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file """
        obj_dict = []
        for obj in type(self).__objects.values():
            obj_dict.append(obj.to_dict())
        with open(type(self).__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        '''"""Deserializes the JSON file to __objects'''
        if exists(type(self).__file_path):
            with open(type(self).__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    obj = self.class_dict[class_name](**value)
                    type(self).__objects[key] = obj
