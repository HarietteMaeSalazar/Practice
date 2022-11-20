import os

clear = lambda: os.system('cls')

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2


def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

operations = {  "+": add, "-": subtract, "*": multiply,  "/": divide}


def calculator():
  num1 = float(input("Enter first number: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Choose the operation you want to perform: ")
    num2 = float(input("Enter second number: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Please type 'yes' if you want to continue calculating with {answer}, or type 'no' if you want  to start a new calculation: ") == 'yes':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()