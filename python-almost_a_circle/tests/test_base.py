#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest

Base = __import__('models.base', fromlist=['Base']).Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

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

    def test_base_id_none(self):
        """Test id assignment when id is None."""
        b4 = Base()
        self.assertEqual(b4.id, 3)

if __name__ == "__main__":
    unittest.main()