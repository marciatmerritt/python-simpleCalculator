import signal

# Define basic arithmetic functions
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return None # Return None if division by zero
  return x / y

def exponentiate(x, y):
  return x ** y

# Function to get operation choice
def get_operation():
  operations = {
    "1": {"name": "Add", "symbol": "+", "function": add},
    "2": {"name": "Subtract", "symbol": "-", "function": subtract},
    "3": {"name": "Multiply", "symbol": "*", "function": multiply},
    "4": {"name": "Divide", "symbol": "/", "function": divide},
    "5": {"name": "Exponentiate", "symbol": "^", "function": exponentiate},
    "0": {"name": "Exit", "symbol": None},
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
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Invalid input. Please enter a valid number.")

# Function to prompt the user to continue or not
def keep_going(prompt="\nWould you like to do another calculation? (yes/no): "):
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

# Set the signal handler for SIGINT (Ctrl+C)
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