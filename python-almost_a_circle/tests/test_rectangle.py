#!/usr/bin/python3
"""
Unit tests for the Rectangle class.
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_rectangle_creation(self):
        """Test normal creation of Rectangle."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_creation_with_invalid_width(self):
        """Test creation with invalid width."""
        with self.assertRaises(ValueError):
            Rectangle("1", 2)
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_creation_with_invalid_height(self):
        """Test creation with invalid height."""
        with self.assertRaises(ValueError):
            Rectangle(1, "2")
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_creation_with_invalid_x_and_y(self):
        """Test creation with invalid x and y."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, "3")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area calculation."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        """Test string representation."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_display(self):
        """Test display method."""
        r = Rectangle(2, 2, 1, 1)
        with self.assertLogs() as log:
            r.display()
        self.assertIn(" # # ", log.output[0])
        self.assertIn("# #", log.output[1])

    def test_to_dictionary(self):
        """Test conversion to dictionary."""
        r = Rectangle(1, 2, 3, 4, 5)
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_update(self):
        """Test the update method."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)

if __name__ == "__main__":
    unittest.main()
