import unittest
from calculator import divide

class TestDivide(unittest.TestCase):
    """Test cases for the divide function"""
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(15, 3), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
    
    def test_divide_negative_numbers(self):
        """Test division involving negative numbers"""
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertEqual(divide(-10, -2), 5.0)
    
    def test_divide_with_zero_numerator(self):
        """Test division when numerator is zero"""
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(0, -3), 0.0)
    
    def test_divide_by_zero(self):
        """Test division by zero cases"""
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(-5, 0)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 0)
    
    def test_divide_floating_point(self):
        """Test division with floating point numbers"""
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333, places=10)
        self.assertEqual(divide(2.5, 0.5), 5.0)
        self.assertAlmostEqual(divide(22, 7), 3.142857142857143, places=10)
    
    def test_divide_large_numbers(self):
        """Test division with very large numbers"""
        self.assertEqual(divide(1000000, 1000), 1000.0)
        self.assertAlmostEqual(divide(1e10, 1e5), 1e5)

if __name__ == '__main__':
    unittest.main()
