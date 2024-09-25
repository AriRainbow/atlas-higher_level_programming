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

    def tearDown(self):
        """Reset __nb_objects after each test to ensure isolation."""
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
        self.assertEqual(b4.id, 1)  # Auto-incremented
        self.assertEqual(b5.id, 100)  # Explicit ID
        self.assertEqual(b6.id, 2)  # Auto-increment

    def test_base_id_auto_increment_continues(self):
        """Test that auto-increment continues correctly after explicit ID assignment."""
        b7 = Base()
        b8 = Base(500)
        b9 = Base()
        self.assertEqual(b7.id, 1)  # Auto
        self.assertEqual(b8.id, 500)  # Explicit
        self.assertEqual(b9.id, 2)  # Auto continues from previous auto

if __name__ == "__main__":
    unittest.main()
