"""
Different types of functions
"""

# No argument function
def shield():
    return 'Hail Hydra!'

print(f'Shield: {shield()}') # Hail Hydra!

# One argument function
def square(x):
    return x ** 2

print(f'3^2 is: {square(3)}') # 9

# Two argument functions
def add(x, y):
    return x + y

print(f'2 + 3 = {add(2, 3)}') # 5

def subtract(x, y):
    return x - y

print(f'3 - 2 = {subtract(3, 2)}') # 1

# Functions with Default Parameters
def math(x, y, fn = add):
    return fn(x, y)

print(f'math(2,3) = {math(2, 3)}') # 5
print(f'math(3,2,subtract) = {math(3, 2, subtract)}') #1

# Syntactic sugar: Keyword arguments
print('Syntactic sugar: Keyword arguments')
print(f'math(x = 5, y =3, fn = add): {math(x = 5, y =3, fn = add)}') # 8
print(f'math(fn = subtract, x = 5, y = 3): {math(fn = subtract, x = 5, y = 3)}') # 2

# Scoping:
age = 26 # scoped globally

def increment_age():
    # The global keyword specified you're referring to a global variable.
    global age # If this is not specified, a local scoped age will be used.
    age += 1
    return age

print(f'increment_age() has incremented age to - {increment_age()}') # 27
print(f'manipulating a global introduces a side-effect: {age}') # 27

# Multi-argument function (*args)
def dangerous_words(*words):
    for word in words:
        print(word)

print('Don\'t mess with me, I know:')
dangerous_words('kung-fu',
                'taekwondo',
                'judo',
                'karatedo',
                'and other dangerous words')

# Multi-argument Keyword Parameters (**kwargs)
def harry_potter_books(**books):
    for key, value in books.items():
        print(f'{key} key has a value of {value}')

print('The first two Hairy Powter books are:')
harry_potter_books(first = 'Sorcerer\'s Stone',
                   second = 'Chamber of Secrets')
