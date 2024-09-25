#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""
import unittest
Rectangle = __import__('models.rectangle', fromlist=['Rectangle']).Rectangle
class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""
    def test_rectangle_creation(self):
        """Test Rectangle instantiation with valid parameters."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
if __name__ == "__main__":
    unittest.main()
