#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest

Base = __import__('models.base', fromlist=['Base']).Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset __nb_objects to 0 before each test to avoid conflicts."""
        Base._Base__nb_objects = 0

    def test_base_id_auto_increment(self):
        """Test automatic id assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_id_explicit(self):
        """Test explicit id assignment."""
        b3 = Base(42)
        self.assertEqual(b3.id, 42)

    def test_base_id_mixed(self):
        """Test mixed automatic and explicit ID assignment."""
        b4 = Base()
        b5 = Base(100)
        b6 = Base()
        self.assertEqual(b4.id, 3)  # Auto-incremented
        self.assertEqual(b5.id, 100)  # Explicit ID
        self.assertEqual(b6.id, 4)  # Auto-increment

if __name__ == "__main__":
    unittest.main()
