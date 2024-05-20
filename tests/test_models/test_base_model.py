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

    def test_instance_creation_from_dict(self):
        '''Test instance creation from dictionary representation'''
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        print("to_ dict")
        print(my_model_dict)
        my_new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)


if __name__ == '__main__':
    unittest.main()
