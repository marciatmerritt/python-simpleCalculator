def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
    return None
  return x / y
    
  
def keep_going(prompt="\nWould you like to do another calculation? (yes/no): "):
  while True:
    response = input(prompt).strip().lower()
    if response in ('yes', 'y'):
      return True
    elif response in ('no', 'n'):
      return False
    else:
      print("Invalid input. Please enter 'yes', 'no', 'y', or 'n'.")

print("Select operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
  choice = input("\nEnter Selection (1/2/3/4/5): ")
  if choice in ('1', '2', '3', '4'):
    try:
      num1 = float(input("Enter first number: "))
      num2 = float(input("Enter second number: "))
    except ValueError:
      print("\nInvalid input. Please enter numbers only")
      continue
    if choice == '1':
      print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
      print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
      print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
      result = divide(num1, num2)
      if result is None:
        print("\nError: Division by zero is not allowed!")
      else:
        print(f"{num1} / {num2} = {result}")
    
  elif choice == '5':
    print("\nExiting the calculator. Goodbye!")
    break
  else:
    print("\nInvalid input. Please enter a valid option (1/2/3/4/5).")
    continue
  
  if not keep_going():
    print("\nExiting the calculator. Goodbye!")
    break
