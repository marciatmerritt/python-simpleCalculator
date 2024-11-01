def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y != 0:
    return x / y
  else:
    print("Division by zero not allowed!")

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
  # get input from user
  choice = input("Enter Selection: ")
  if choice in ('1', '2', '3', '4'):
    try:
      # get numbers from the user
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("Invalid input. Please enter a number")
      continue

  else:
    print("Invalid input. Try Again")