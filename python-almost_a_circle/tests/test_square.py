#!/usr/bin/python3
"""
Unit tests for the Square class.
"""
import unittest
Square = __import__('models.square', fromlist=['Square']).Square

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_square_creation(self):
        """Test Square instantiation with valid parameters."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_creation_with_too_few_arguments(self):
        """Test instantiation with too few arguments."""
        with self.assertRaises(TypeError):
            Square()

    def test_square_creation_with_too_many_arguments(self):
        """Test instantiation with too many arguments."""
        with self.assertRaises(TypeError):
            Square(1, 2)

    def test_square_creation_with_negative_size(self):
        """Test instantiation with negative size."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_creation_with_zero_size(self):
        """Test instantiation with zero size."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_area(self):
        """Test the area method."""
        s = Square(2)
        self.assertEqual(s.area(), 4)

    def test_str(self):
        """Test the __str__ method."""
        s = Square(2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")

    def test_update(self):
        """Test the update method."""
        s = Square(2)
        s.update(89, 3)
        self.assertEqual(s.size, 3)

if __name__ == "__main__":
    unittest.main()