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

    def test_rectangle_creation_with_invalid_width(self):
        """Test instantiation with an invalid width."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_creation_with_invalid_height(self):
        """Test instantiation with an invalid height."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_creation_with_invalid_x(self):
        """Test instantiation with an invalid x."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_creation_with_invalid_y(self):
        """Test instantiation with an invalid y."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_creation_with_too_many_arguments(self):
        """Test instantiation with too many arguments."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5)

if __name__ == "__main__":
    unittest.main()
