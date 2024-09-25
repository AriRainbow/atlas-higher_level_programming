#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    @classmethod
    def setUpClass(cls):
        """Runs once for the entire test class to initialize any class-wide state."""
        cls._original_nb_objects = Base._Base__nb_objects

    def setUp(self):
        """Runs before each test to reset the _nb_objects counter."""
        Base._Base__nb_objects = 0

    def test_auto_id_assignment(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_explicit_id_assignment(self):
        """Test explicit ID assignment."""
        b1 = Base(100)
        self.assertEqual(b1.id, 100)

    def test_mixed_id_assignment(self):
        """Test mixed automatic and explicit ID assignment."""
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 42)
        self.assertEqual(b3.id, 2)

    def test_reset_nb_objects(self):
        """Test that the _nb_objects is correctly reset between tests."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    @classmethod
    def tearDownClass(cls):
        """Runs once after all tests to clean up any modifications."""
        Base._Base__nb_objects = cls._original_nb_objects

if __name__ == "__main__":
    unittest.main()