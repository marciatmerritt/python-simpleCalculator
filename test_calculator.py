import unittest
from io import StringIO
from unittest.mock import patch
from calculator import add, subtract, multiply, divide, exponentiate, get_operation, get_number, keep_going, main

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 4), 4)
    
    def test_add_edge_cases(self):
        self.assertEqual(add(0.1, 0.2), 0.3)
        self.assertEqual(add(float('inf'), float('inf')), float("inf"))
        self.assertEqual(add(float('-inf'), float('-inf')), float("-inf"))

    def test_subtract(self):
        self.assertEqual(subtract(3, 3.5), -0.5)
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
        self.assertEqual(divide(10, 3), 3.333)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)

    def test_divide_by_zero_returns_none(self):
        self.assertIsNone(divide(1, 0))
    
    def test_exponentiate(self):
        self.assertEqual(exponentiate(25, 2), 625)
        self.assertEqual(exponentiate(2, -3), 0.125)
        self.assertEqual(exponentiate(4, 2), 16)

    def test_exponentiate_edge_cases(self):
        self.assertEqual(exponentiate(0, 0), 1)
        self.assertEqual(exponentiate(4, 0), 1)
        self.assertEqual(exponentiate(50, 4), 6250000)
        self.assertEqual(exponentiate(-1, -1), -1)
        self.assertEqual(exponentiate(-1, 1), -1)
        self.assertEqual(exponentiate(4, 0.5), 2)
    
    @patch("builtins.input", side_effect=['0'])
    @patch("builtins.print")
    def test_get_operation_menu_display(self, mock_print, mock_input):
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

    @patch("builtins.print")
    def test_get_operation_all_options(self, mock_print):
      operations = {
        '1': {"name": "Add", "symbol": "+", "function": add},
        '2': {"name": "Subtract", "symbol": "-", "function": subtract},
        '3': {"name": "Multiply", "symbol": "*", "function": multiply},
        '4': {"name": "Divide", "symbol": "/", "function": divide},
        '5': {"name": "Exponentiate", "symbol": "^", "function": exponentiate},
        '0': {"name": "Exit", "symbol": None, "function": None}
      }

    # Loop through each operation input, using subTest to test each operation
      for input_value, expected in operations.items():
        with self.subTest(input_value = input_value):
            with patch("builtins.input", side_effect=[input_value]):
                operation = get_operation()
                self.assertEqual(operation['name'], expected["name"])
                self.assertEqual(operation['symbol'], expected["symbol"])
                self.assertEqual(operation['function'], expected["function"])

    @patch("builtins.input", side_effect=['$', '?', '0'])
    @patch("builtins.print")
    def test_get_operation_invalid_then_valid_selection(self, mock_print, mock_input):
       operation = get_operation()
       mock_print.assert_any_call("\nInvalid selection. Please choose a valid option.")
       self.assertEqual(operation['name'], "Exit")


    @patch("builtins.input", side_effect=['1.2'])
    @patch("builtins.print")
    def test_get_number_valid_input(self, mock_print, mock_input):
        result = get_number("Enter Number: ")
        self.assertEqual(result, 1.2)

    @patch("builtins.input", side_effect=['a', '2'])
    @patch("builtins.print")
    def test_get_number_invalid_then_valid_input(self, mock_print, mock_input):
        result = get_number("Enter Number: ")
        mock_print.assert_called_with("Invalid input. Please enter numbers only.")
        self.assertEqual(result, 2.0)

    @patch("builtins.input", side_effect=['a', 'b', '9'])
    @patch("builtins.print")
    def test_get_number_with_multiple_invalid_then_valid_input(self, mock_print, mock_input):
        result = get_number("Enter Number: ")
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("Invalid input. Please enter numbers only.")
        self.assertEqual(result, 9.0)

    @patch("builtins.input", side_effect=['yes', 'y', 'YeS ', 'YES', 'Y'])
    @patch("builtins.print")
    def test_keep_going_all_yes(self, mock_print, mock_input):
        for _ in range(5):
            self.assertTrue(keep_going())

    @patch("builtins.input", side_effect=['no', 'n', 'No', 'NO', 'N'])
    @patch("builtins.print")
    def test_keep_going_all_no(self, mock_print, mock_input):
        for _ in range(5):
            self.assertFalse(keep_going())

    @patch("builtins.input", side_effect=['help', 'y'])
    @patch("builtins.print")
    def test_keep_going_invalid_then_yes(self, mock_print, mock_input):
        result = keep_going("Continue?")
        mock_print.assert_called_with("Invalid input. Please enter 'yes', 'no', 'y', or 'n'.")
        self.assertTrue(result)


    @patch("builtins.input", side_effect=['1', '2', '3', 'No'])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_addition_workflow_correct_output(self, mock_stdout, mock_input):
        main()        
        output = mock_stdout.getvalue()
        
        self.assertIn("Select operation: ", output)
        self.assertIn("2.0 + 3.0 = 5.0", output)
        self.assertIn("Exiting the calculator. Goodbye!", output)
    
    @patch("builtins.input", side_effect=['4', '10', '0', 'No'])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_divide_by_zero(self, mock_stdout, mock_input):
        main()        
        output = mock_stdout.getvalue()
        
        self.assertIn("Select operation: ", output)
        self.assertIn("Error: Division by zero is not allowed!", output)
        self.assertIn("Exiting the calculator. Goodbye!", output)
        
    @patch("builtins.input", side_effect=['4', '10', '100', 'Y', '3', '10', '100', 'n'])
    @patch("sys.stdout", new_callable=StringIO)
    def test_main_multiple_operations(self, mock_stdout, mock_input):
        main()
        # Capture the printed output for verification
        output = mock_stdout.getvalue()
        
        # Check if the operation selection menu is displayed initially
        self.assertIn ("Select operation: ", output)
        # First operation is division ( 10 / 100 )
        self.assertIn("10.0 / 100.0 = 0.1", output)

        # After the first calculation, the user chose to continue ('Y')
        # The next operation is multiplication (10 * 100)
        self.assertIn("10.0 * 100.0 = 1000.0", output)

        # After the second calculation, the user chose not to continue ('n')
        # Verify that the calculator exits with the appropriate goodbye message
        self.assertIn("Exiting the calculator. Goodbye!", output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
