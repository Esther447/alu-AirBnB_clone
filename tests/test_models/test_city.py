#!/usr/bin/python3
"""Unit tests for City class"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test City model"""

    def test_instance(self):
        city = City()
        self.assertIsInstance(city, City)

if __name__ == "__main__":
    unittest.main()
