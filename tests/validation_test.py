import unittest
from handle.validations import check_values

class TestCheckValues(unittest.TestCase):
    def test_valid_values(self):
        self.assertIsNone(check_values(10, 5, 2))
    
    def test_inputs_not_numbers(self):
        self.assertEqual(check_values("abc", 5, 2), "All inputs must be numbers")
        self.assertEqual(check_values(10, "xyz", 2), "All inputs must be numbers")
        self.assertEqual(check_values(10, 5, "qwe"), "All inputs must be numbers")
    
    def test_values_less_than_or_equal_zero(self):
        self.assertEqual(check_values(0, 5, 2), "High must be greater than 0")
        self.assertEqual(check_values(-10, 5, 2), "High must be greater than 0")
        self.assertEqual(check_values(10, 0, 2), "Low must be greater than 0")
        self.assertEqual(check_values(10, -5, 2), "Low must be greater than 0")
        self.assertEqual(check_values(10, 5, 0), "Risk must be greater than 0")
        self.assertEqual(check_values(10, 5, -1), "Risk must be greater than 0")
    
    def test_low_greater_than_or_equal_high(self):
        self.assertEqual(check_values(10, 10, 2), "Low can't be bigger than High")
        self.assertEqual(check_values(10, 15, 2), "Low can't be bigger than High")
    
if __name__ == "__main__":
    unittest.main()
