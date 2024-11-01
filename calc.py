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
    if choice == '1':
      print(num1, " + ", num2, " = ", add(num1, num2))
    elif choice == '2':
      print(num1, " - ", num2, " = ", subtract(num1, num2))
    elif choice == '3':
      print(num1, " * ", num2, " = ", multiply(num1, num2))
    elif choice == '4':
      try:  
        print(num1, " / ", num2, " = ", divide(num1, num2))
      except ZeroDivisionError:
        print("Division by zero not allowed!")
        continue
    
    next_calculation = input("Would you like to do another calculation? ")
    if next_calculation == 'no':
      break
  else:
    print("Invalid input. Try Again")
  
