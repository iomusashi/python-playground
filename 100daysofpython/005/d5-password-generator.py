import random

letters = [
    'a', 'b', 'c', 'd', 'e', 
    'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 
    'p', 'q', 'r', 's', 't', 
    'u', 'v', 'w', 'x', 'y', 
    'z', 
    'A', 'B', 'C', 'D', 'E', 
    'F', 'G', 'H', 'I', 'J', 
    'K', 'L', 'M', 'N', 'O', 
    'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 
    'Z'
]
numbers = [
    '0', '1', '2', '3', '4', 
    '5', '6', '7', '8', '9'
]
symbols = [
    '!', '#', '$', '%', '&', 
    '(', ')', '*', '+'
]

print('Welcome to the PyPassword Generator!')

letter_count = int(input('How many letters would you like in your password? '))
number_count = int(input('How many numbers would you like? '))
symbol_count = int(input('How many symbols would you like? '))

password = []

for char in range(0, letter_count):
    password.append(random.choice(letters))

for char in range(0, number_count):
    password.append(random.choice(numbers))

for char in range(0, symbol_count):
    password.append(random.choice(symbols))

print(password)
random.shuffle(password)
print(password)

generated = ''
for char in password:
    generated += char

print(f'Your password is: {generated}')
