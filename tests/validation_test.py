import unittest
from handle.validations import check_values

class TestCheckValues(unittest.TestCase):
    def test_valid_values(self):
        self.assertIsNone(check_values(10, 5, 2))
    
    def test_high_not_a_number(self):
        self.assertEqual(check_values("abc", 5, 2), "High must be a Number")
    
    def test_low_not_a_number(self):
        self.assertEqual(check_values(10, "xyz", 2), "Low must be a Number")
    
    def test_risk_not_a_number(self):
        self.assertEqual(check_values(10, 5, "qwe"), "Risk must be a Number")
    
    def test_low_greater_than_or_equal_high(self):
        self.assertEqual(check_values(10, 10, 2), "Low cant be bigger than High")
        self.assertEqual(check_values(10, 15, 2), "Low cant be bigger than High")
    
if __name__ == "__main__":
    unittest.main()
