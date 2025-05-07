#!/usr/bin/python3
"""Unit tests for Amenity class"""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test Amenity model"""

    def test_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

if __name__ == "__main__":
    unittest.main()
