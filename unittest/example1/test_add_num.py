import unittest
from add_num import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-5, -3), -8)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add_numbers(2, -3), -1)

if __name__ == '__main__':
    unittest.main()

