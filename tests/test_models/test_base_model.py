#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""

    def test_instance(self):
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

if __name__ == "__main__":
    unittest.main()
