#!/usr/bin/python3
"""Unit tests for Review class"""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test Review model"""

    def test_instance(self):
        review = Review()
        self.assertIsInstance(review, Review)

if __name__ == "__main__":
    unittest.main()
