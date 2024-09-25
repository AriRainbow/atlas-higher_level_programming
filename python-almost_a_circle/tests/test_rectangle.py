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

    def test_rectangle_creation_with_negative_width(self):
        """Test instantiation with a negative width."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_creation_with_negative_height(self):
        """Test instantiation with a negative height."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_creation_with_zero_width(self):
        """Test instantiation with a width of zero."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_creation_with_zero_height(self):
        """Test instantiation with a height of zero."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_creation_with_negative_x(self):
        """Test instantiation with a negative x-coordinate."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_creation_with_negative_y(self):
        """Test instantiation with a negative y-coordinate."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

if __name__ == "__main__":
    unittest.main()
