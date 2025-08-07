import unittest
from calculator import divide

class TestDivide(unittest.TestCase):
    
    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    
    def test_divide_with_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0, -3), 0.0)
    
    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), "Division by zero error")
        self.assertEqual(divide(-5, 0), "Division by zero error")
        self.assertEqual(divide(0, 0), "Division by zero error")
    
    def test_divide_floating_point(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333)
        self.assertEqual(divide(2.5, 0.5), 5.0)

if __name__ == '__main__':
    unittest.main()