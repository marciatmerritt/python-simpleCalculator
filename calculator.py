import signal

"""Calculator Module.

This module provides basic arithmetic functions: addition, subtraction,
multiplication, division, and exponentiation.
"""
def add(x, y):
  return round((x + y), 3)

def subtract(x, y):
  return round((x - y), 3)

def multiply(x, y):
  return round((x * y), 3)

def divide(x, y):
  """Divide two numbers.

  Parameters:
      x (float): The numerator.
      y (float): The denominator. Must not be zero.

  Returns:
      float or None: The result of dividing x by y, or None if y is zero.
  """
  if y == 0:
    return None # Avoid division by zero
  return round((x / y), 3)

def exponentiate(x, y):
  return round((x ** y), 3)

def get_operation():
  """Display a menu of operations and prompt the user to choose one.

  Returns the dictionary entry (operation) based on user's choice.
  """
  # Dictionary of operations, where each key is a string for selection
  operations = {
    "1": {"name": "Add", "symbol": "+", "function": add},
    "2": {"name": "Subtract", "symbol": "-", "function": subtract},
    "3": {"name": "Multiply", "symbol": "*", "function": multiply},
    "4": {"name": "Divide", "symbol": "/", "function": divide},
    "5": {"name": "Exponentiate", "symbol": "^", "function": exponentiate},
    "0": {"name": "Exit", "symbol": None, "function": None},
  }

  print("\nSelect operation: ")
  for key, value in operations.items():
    print(f"{key}. {value['name']}")
  
  while True:
    choice = input("\nEnter Operation Selection: ")
    if choice in operations:
      return operations[choice]
    print("\nInvalid selection. Please choose a valid option.")

def get_number(prompt):
  """Prompt the user to enter a number and keep asking until a valid number is entered.

  Returns the number as a float.
  """
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Invalid input. Please enter numbers only.")


def keep_going(prompt="\nWould you like to do another calculation? (yes/no): "):
  """Prompt the user to continue or exit.

  Returns True to continue, False to exit.
  """
  while True:
    response = input(prompt).strip().lower()
    if response in ('yes', 'y'):
      return True
    elif response in ('no', 'n'):
      return False
    else:
      print("Invalid input. Please enter 'yes', 'no', 'y', or 'n'.")

# Signal handler for graceful exit on Ctrl+C
def signal_handler(sig, frame):
    print('\nCtrl+C pressed \nExiting the calculator. Goodbye!')
    exit(0)

# Set signal handle for SIGINT (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Main function to run the calculator program
def main():
    while True:
      choice = get_operation()
      if choice['name'] == "Exit":
        print("\nExiting the calculator. Goodbye!")
        break
      
      # prompt user for numbers
      num1 = get_number("Enter first number: ")
      num2 = get_number("Enter second number: ")

      # perform calculations
      result = choice['function'](num1, num2)
      if result is None and choice['name'] == "Divide":
        print("Error: Division by zero is not allowed!")
      else:
        print(f"{num1} {choice['symbol']} {num2} = {result}")
    
      if not keep_going():
        print("\nExiting the calculator. Goodbye!")
        break

# Run the main function if the script is executed directly
if __name__ == "__main__":
  main()