#!/usr/bin/python3
"""
Unittest for max_integer function.
"""
import unittest

# Import the max_integer function dynamically
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_positive_integers(self):
        """Test list with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_integers(self):
        """Test list with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test list with mixed positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        """Test list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list."""
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        """Test list with float values."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_types(self):
        """Test list with integers and floats."""
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_strings(self):
        """Test list with strings (should return the max string)."""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

if __name__ == "__main__":
    unittest.main()
