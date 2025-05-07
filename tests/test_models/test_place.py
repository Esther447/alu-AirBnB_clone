#!/usr/bin/python3
"""Unit tests for Place class"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test Place model"""

    def test_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)

if __name__ == "__main__":
    unittest.main()
