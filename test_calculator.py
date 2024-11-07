import unittest
import sys
from unittest.mock import patch
from calculator import add, subtract, multiply, divide, exponentiate, get_operation, get_number, keep_going

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 4), 4)

    def test_subtract(self):
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 4), -4)
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(4, 0), 0)
    
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(10, 3), 3.33, places=3)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        self.assertIsNone(divide(1, 0))
    
    def test_exponentiate(self):
        self.assertEqual(exponentiate(25, 2), 625)
        self.assertAlmostEqual(exponentiate(2, -3), 0.125, places=3)
        self.assertEqual(exponentiate(4, 2), 16)
        """Test exponentiate edge cases"""
        self.assertEqual(exponentiate(0, 0), 1)
        self.assertEqual(exponentiate(4, 0), 1)
        self.assertEqual(exponentiate(50, 4), 6250000)
        self.assertEqual(exponentiate(-1, -1), -1)
        self.assertEqual(exponentiate(-1, 1), -1)
        self.assertEqual(exponentiate(4, 0.5), 2)
    
    @patch("builtins.input", side_effect=['0'])
    @patch("builtins.print")
    def test_get_operation_prints_all_selections(self, mock_print, mock_input):
        get_operation()
        printed_lines = [call[0][0] for call in mock_print.call_args_list]
        expected_lines = [
            "\nSelect operation: ",
            "1. Add",
            "2. Subtract",
            "3. Multiply",
            "4. Divide",
            "5. Exponentiate",
            "0. Exit"
        ]

        for line in expected_lines:
            self.assertIn(line, printed_lines)


    @patch("builtins.input", side_effect=['1'])
    @patch("builtins.print")
    def test_get_operation_add(self, mock_print, mock_input):
       operation = get_operation()
       self.assertEqual(operation['name'], "Add")
       self.assertEqual(operation['symbol'], "+")
       self.assertEqual(operation['function'], add)
    
    @patch("builtins.input", side_effect=['2'])
    @patch("builtins.print")
    def test_get_operation_subtract(self, mock_print, mock_input):
       operation = get_operation()
       self.assertEqual(operation['name'], "Subtract")
       self.assertEqual(operation['symbol'], "-")
       self.assertEqual(operation['function'], subtract)
    
    @patch("builtins.input", side_effect=['3'])
    @patch("builtins.print")
    def test_get_operation_multiply(self, mock_print, mock_input):
       operation = get_operation()
       self.assertEqual(operation['name'], "Multiply")
       self.assertEqual(operation['symbol'], "*")
       self.assertEqual(operation['function'], multiply)
    
    @patch("builtins.input", side_effect=['4'])
    @patch("builtins.print")
    def test_get_operation_divide(self, mock_print, mock_input):
       operation = get_operation()
       self.assertEqual(operation['name'], "Divide")
       self.assertEqual(operation['symbol'], "/")
       self.assertEqual(operation['function'], divide)
    
    @patch("builtins.input", side_effect=['5'])
    @patch("builtins.print")
    def test_get_operation_exponentiate(self, mock_print, mock_input):
       operation = get_operation()
       self.assertEqual(operation['name'], "Exponentiate")
       self.assertEqual(operation['symbol'], "^")
       self.assertEqual(operation['function'], exponentiate)
    
    @patch("builtins.input", side_effect=['0'])
    @patch("builtins.print")
    def test_get_operation_exit(self, mock_print, mock_input):
       operation = get_operation()
       self.assertEqual(operation['name'], "Exit")
       self.assertEqual(operation['symbol'], None)

    @patch("builtins.input", side_effect=['$', '?', '0'])
    @patch("builtins.print")
    def test_get_operation_invalid_then_valid_selection(self, mock_print, mock_input):
       operation = get_operation()
       mock_print.assert_any_call("\nInvalid selection. Please choose a valid option.")
       self.assertEqual(operation['name'], "Exit")


    @patch("builtins.input", side_effect=['1.2'])
    @patch("builtins.print")
    def test_get_number_with_valid_input(self, mock_print, mock_input):
        result = get_number("Enter Number: ")
        self.assertEqual(result, 1.2)

    @patch("builtins.input", side_effect=['a', '2'])
    @patch("builtins.print")
    def test_get_number_with_invalid_then_valid_input(self, mock_print, mock_input):
        result = get_number("Enter Number: ")
        mock_print.assert_called_with("Invalid input. Please enter numbers only.")
        self.assertRaises(ValueError)
        self.assertEqual(result, 2.0)

    @patch("builtins.input", side_effect=['a', 'b', '9'])
    @patch("builtins.print")
    def test_get_number_with_multiple_invalid_then_valid_input(self, mock_print, mock_input):
        result = get_number("Enter Number: ")
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_called_with("Invalid input. Please enter numbers only.")
        self.assertRaises(ValueError)
        self.assertEqual(result, 9.0)

    @patch("builtins.input", side_effect=['yes', 'y', 'YeS ', 'YES', 'Y'])
    @patch("builtins.print")
    def test_keep_going_with_yes(self, mock_print, mock_input):
        for _ in range(5):
            self.assertTrue(keep_going())

    @patch("builtins.input", side_effect=['no', 'n', 'No', 'NO', 'N'])
    @patch("builtins.print")
    def test_keep_going_with_no(self, mock_print, mock_input):
        for _ in range(5):
            self.assertFalse(keep_going())

    @patch("builtins.input", side_effect=['help', 'y'])
    @patch("builtins.print")
    def test_keep_going_with_invalid_input_then_yes(self, mock_print, mock_input):
        result = keep_going("Continue?")
        mock_print.assert_called_with("Invalid input. Please enter 'yes', 'no', 'y', or 'n'.")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main(verbosity=2)
