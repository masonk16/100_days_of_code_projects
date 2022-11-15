# Calculator
from art import logo
#Addition
def add(n1, n2):
  """Takes 2 numbers, adds them and returns the result."""
  return n1 + n2

#Subtraction
def subtract(n1, n2):
  """Takes 2 numbers, subtracts the first from the second and returns the result."""
  return n1 - n2

#Multiplication
def multiply(n1, n2):
  """Takes 2 numbers, multiplies them and returns the result."""
  return n1 * n2

#Division
def divide(n1, n2):
  """Takes 2 numbers, divides the first by the second and returns the result."""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  keep_running = True
  
  while keep_running:
    operation_symbol = input("Pick an operation from above: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    carry_on = input(f"Type 'y' to carry on calculating with {answer}, or 'n' to start a new calculation.")
    if carry_on == "y":
      num1 = answer
    else:
      keep_running = False
      calculator()

calculator()      