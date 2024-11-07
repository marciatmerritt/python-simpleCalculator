# Simple ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) Calculator

## Table of Contents

- [Overview](#overview)
- [What I Learned](#what-i-learned)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)
- [License](#license)
- [Version History](#version-history)

## Overview

 This is my first practice project in Python, aimed at learning fundamental programming concepts including operators, functions, control flow, and loops. This simple command-line calculator allows users to perform basic arithmetic operations and provides error handling for various types of input.

 As part of this project, I spent a significant amount of time learning how to write tests for my code using Python's built-in `unittest` framework. Writing tests helped ensure that each function in the calculator performs as expected and allowed me to validate my logic for edge cases and potential errors.

## What I Learned

Through this project, I practiced:

- **Python Operators**: Implementing basic arithmetic operations.
- **Functions and Function Arguments**: Writing functions for each operation (addition, subtraction, multiplication, and division) and passing arguments to them.
- **User-Defined Functions**: Defining functions to organize code, making it reusable and modular.
- **Control Flow**: Using `if-else` statements to handle different user selections and input validation.
- **Loops**: Implementing a `while` loop to keep the program running until the user decides to exit.
- **Error Handling**: Managing potential errors, such as non-numeric inputs and division by zero.
- **Testing with `unittest`**: I spent a significant amount of time learning how to use Python's `unittest` framework to write tests for each of my calculator functions. Writing and running tests ensured the reliability and correctness of my code, and helped me identify and fix potential bugs early in the development process. This also helped me become more familiar with the process of test-driven development (TDD).

## Features

- **Basic Arithmetic Operations**:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Exponentiation (`^`)

- **Error Handling**:
  - Handles invalid numeric inputs.
  - Avoids division by zero and provides an error message if division by zero is attempted.

- **User Interaction**:
  - Allows the user to select an operation from a list of options.
  - Prompts the user for two numbers, performs the selected operation, and displays the result.
  - After each operation, the user is prompted whether they want to continue with another calculation or exit.

## Installation

1. **Clone or Download the Repository**
   - Clone the repository using Git:

     ```bash
     git clone https://github.com/marciatmerritt/python-simpleCalculator.git
     ```

   - Or download the ZIP file from GitHub and extract it to your preferred directory.

2. **Navigate to the Project Directory**

   ```bash
   cd python-simpleCalculator
   ```

3. **Run the Script**
   - Ensure you have Python 3.x installed on your computer. Check your Python version by running:

     ```bash
     python --version
     ```

## Usage

### How to Use

1. Run the script using a Python interpreter.

   ```bash
   python calculator.py
   ```

2. **Menu Display**:

- The user is prompted to select an operation by entering the corresponding number of the item on the menu display.

3. **Input Numbers**:

   - After selecting an operation, the user is prompted to enter two numbers for the operation.

4. **Display Results**:
   - The result is displayed, and the user is asked if they wish to perform another operation or exit.

5. **Exit or Continue**:
   - After each operation, the user can choose to continue with another calculation or exit by entering `no` or `n`.

### Code Overview

- **Functions**:
  - The functions for basic operations (`add`, `subtract`, `multiply`, `divide`, `exponentiate`) ensure the calculations are done and rounded to three decimal places.
  
- **`get_number` Function**:
  - This function handles user input for numbers, ensuring valid numeric input.

- **`get_operation` Function**:
  - This function presents a menu of operations and waits for the user to choose one. It ensures only valid options are selected.

- **Graceful Exit on `Ctrl+C`**:
  - A signal handler is implemented to catch a `Ctrl+C` interrupt (SIGINT) and display a friendly exit message.

### Example Use Case

```plaintext
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponentiate
0. Exit

Enter Operation Selection: 1
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
Would you like to do another calculation? (yes/no): no
Exiting the calculator. Goodbye!
```

---

## Requirements

[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=ffdd54)](https://python.org "Go to Python homepage")

## Error Handling

- **Division by Zero**: If the user attempts to divide by zero, the program displays an error message and skips the calculation.
- **Invalid Input**: Non-numeric inputs trigger a prompt asking the user to enter a valid number.
- **Invalid Selection**: If an invalid option is selected, the program will prompt the user to enter a valid choice.

## Testing

To ensure the reliability and correctness of the calculator, basic tests have been added for different operations. Here are a few examples of the tests:

### Test Cases

1. **Addition**: 
   - Input: `10 + 5`
   - Expected Output: `15.0`

2. **Subtraction**:
   - Input: `15 - 5`
   - Expected Output: `10.0`

3. **Multiplication**:
   - Input: `10 * 5`
   - Expected Output: `50.0`

4. **Division**:
   - Input: `10 / 2`
   - Expected Output: `5.0`

5. **Exponentiation**:
   - Input: `2 ^ 3`
   - Expected Output: `8.0`

6. **Division by Zero**:
   - Input: `10 / 0`
   - Expected Output: `Error: Division by zero is not allowed!`

7. **Invalid Input**:
   - Input: `abc + 10`
   - Expected Output: `Invalid input. Please enter numbers only.`

### Running Tests

You can run the tests using a testing framework such as `unittest`. To run the tests:

1. Create a file named `test_calculator.py`.
2. Write the test functions in this file, using the standard `unittest` framework, e.g., `unittest.TestCase`.
3. Run the tests by executing:

   ```bash
   python -m unittest test_calculator.py
   ```

## Contributing

This is a beginner-friendly project, and contributions are welcome. If you’d like to add more functions (such as exponentiation, square roots, etc.) or improve the user interface, feel free to submit a pull request!

## Acknowledgements

- Special thanks to [Programiz](https://www.programiz.com/python-programming/examples/calculator) for providing an excellent resource on building a calculator in Python, which served as a foundation for this project.
- Thanks to the Python community for their extensive documentation and tutorials that made learning this language accessible and enjoyable.

## Authors

Marcia Merritt

[![LinkedIn][Linkedin]][linkedin-url]

## License

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

## Version History

- 0.1
  - Initial Release 11/01/2024

<!--Markdown Links and Images -->
[Linkedin]: https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/marcia-merritt-58662761/
