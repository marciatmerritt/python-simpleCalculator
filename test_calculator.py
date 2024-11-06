import unittest
from unittest.mock import Mock, patch
from calculator import add, subtract, multiply, divide, exponentiate, get_operation, get_number, keep_going

class TestCalculator(unittest.TestCase):
    mock = Mock()

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(3, 3), 1)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertIsNone(divide(1, 0))
    
    def test_exponentiate(self):
        self.assertEqual(exponentiate(2, 2), 4)
        self.assertEqual(exponentiate(-1, 1), -1)
        self.assertEqual(exponentiate(-1, -1), -1)
        self.assertEqual(exponentiate(25, 2), 625)
    

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
