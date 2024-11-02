# Simple ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) Calculator

## Table of Contents

- [Overview](#overview)
- [What I Learned](#what-i-learned)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Authors](#authors)
- [License](#license)
- [Version History](#version-history)

## Overview

 This is my first practice project in Python, aimed at learning fundamental programming concepts including operators, functions, control flow, and loops. This simple command-line calculator allows users to perform basic arithmetic operations and provides error handling for various types of input.

## What I Learned

Through this project, I practiced:

- **Python Operators**: Implementing basic arithmetic operations.
- **Functions and Function Arguments**: Writing functions for each operation (addition, subtraction, multiplication, and division) and passing arguments to them.
- **User-Defined Functions**: Defining functions to organize code, making it reusable and modular.
- **Control Flow**: Using `if-else` statements to handle different user selections and input validation.
- **Loops**: Implementing a `while` loop to keep the program running until the user decides to exit.
- **Error Handling**: Managing potential errors, such as non-numeric inputs and division by zero.

## Features

- **Basic Arithmetic Operations**:
  - Addition
  - Subtraction
  - Multiplication
  - Division

- **User Interaction & Looping**:
  - Prompts for selecting operations and entering numbers, with an exit option
  - Users can perform additional calculations or exit after each operation, with prompts for valid selections.

- **Input Validation**:
  - Handles non-numeric inputs and division by zero with informative error messages.

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

1. Run the script using a Python interpreter.

   ```bash
   python calculator.py
   ```

2. You’ll be prompted to select an operation by entering a number (1 for addition, 2 for subtraction, etc.).
3. Enter the first and second numbers when prompted.
4. The result of the operation will be displayed.
5. The program will ask if you want to perform another calculation. Enter `yes`, `y`, `no`, or `n` to continue or exit.

### Example

```text
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide

Enter Selection (1/2/3/4): 1
Enter first number: 10
Enter second number: 5
10.0 + 5.0 = 15.0
Would you like to do another calculation? (yes/no): no
Exiting the calculator. Goodbye!
```

## Requirements

- Python 3.x

## Error Handling

- **Division by Zero**: If the user attempts to divide by zero, the program displays an error message and skips the calculation.
- **Invalid Input**: Non-numeric inputs trigger a prompt asking the user to enter a valid number.
- **Invalid Selection**: If an invalid option is selected, the program will prompt the user to enter a valid choice.

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