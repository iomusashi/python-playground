print('Welcome to Python Pizza Deliveries!')

size = input('What size of pizza do you want - S, M, L? ')
add_peperoni = input('Do you want pepperoni - Y or N? ')
extra_cheese = input('Do you want extra cheese - Y or N? ')

show_error = False
final_bill = 0

if size == 'S':
    final_bill += 15
elif size == 'M':
    final_bill += 20
elif size == 'L':
    final_bill += 25
else:
    show_error = True

if add_peperoni == 'Y' and size == 'S':
    final_bill += 2
else:
    final_bill += 3


if extra_cheese == 'Y':
    final_bill += 1

if show_error:
    print('Please choose the correct size.')
else:
    print(f'Your final bill is: ${final_bill}.')
