#!/usr/bin/env python3
import sys
import os
import unittest
# Add the parent directory of the tests folder to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

if __name__ == '__main__':
    import unittest
    unittest.main()
