#!/usr/bin/python3
"""Unit tests for State class"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test State model"""

    def test_instance(self):
        state = State()
        self.assertIsInstance(state, State)

if __name__ == "__main__":
    unittest.main()
