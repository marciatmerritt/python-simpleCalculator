import unittest
from unittest.mock import Mock, patch
from calculator import add, subtract, multiply, divide, keep_going

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
    
    @patch('builtins.input', side_effect = ['yes', 'y', 'YES', 'Y', 'Yes'])
    def test_keep_going_yes(self, mock_input):
        # Should return True for any 'yes' variation
        for _ in range(5):
            self.assertTrue(keep_going())
    
    @patch('builtins.input', side_effect = ['no', 'n', 'NO', 'N', 'No'])
    def test_keep_going_no(self, mock_input):
        # Should return False for any 'no' variation
        for _ in range(5):
            self.assertFalse(keep_going())
    
    @patch('builtins.input', side_effect=['1', 'a', '5'])
    def test_invalid_input_handling(self, mock_input):
        # Simulates entering a non-numeric value first, then a valid number
        with patch('builtins.print') as mock_print:
            with self.assertRaises(ValueError):
                add(input("Enter first number: "), input("Enter second number: "))
            # Extract the actual printed messages
            printed_messages = [call[0][0] for call in mock_print.call_args_list]
            print(printed_messages)
            self.assertIn("\nInvalid input. Please enter numbers only", printed_messages)

    

    
if __name__ == '__main__':
    unittest.main(verbosity=2)
