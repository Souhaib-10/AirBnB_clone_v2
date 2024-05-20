#!/usr/bin/python3
''' define unittests for base_model.py.'''
import unittest
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    ''' unittest for all functionality of  BaseModel class.'''

    def test_constructor(self):
        '''Test instance'''
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str_method(self):
        ''' Test str method'''
        model = BaseModel()
        expect_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expect_str)

    def test_save_method(self):
        '''test save method'''
        model = BaseModel()
        initial_update = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_update)

    def test_to_dict_method(self):
        '''test to_dict method'''
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)


if __name__ == '__main__':
    unittest.main()
