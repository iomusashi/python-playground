from d10_calculator_art import logo

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  return x / y

def valid_operators():
  return ['+', '-', '*', '/']

def is_operator_valid(operator):
  return operator in valid_operators()

def operation(op):
  operations = [add, subtract, multiply, divide]
  return operations[valid_operators().index(op)]

def calculate(x, y, op):
  result = operation(op)(x, y)
  return result

print(logo)
n1 = int(input('What\'s the first number? '))

print('+\n-\n*\n/')
op = input('Pick an operation: ')
if not is_operator_valid(op):
  raise SystemExit()

n2 = int(input('What\'s the second number? '))
print(f'{n1} {op} {n2} = {calculate(n1, n2, op)}')
