def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


number = int(input('Enter a number: '))
if is_prime(number):
    print('It\'s a prime number.')
else:
    print('It\'s not a prime number.')
