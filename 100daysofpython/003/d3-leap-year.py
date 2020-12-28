year = int(input('Which year do you want to check? '))

is_divisible_by_4 = year % 4 == 0
not_divisible_by_100 = year % 100 != 0
is_divisible_by_400 = year % 400 == 0

is_leap_year = is_divisible_by_4 and (
    not_divisible_by_100 or is_divisible_by_400)

if is_leap_year:
    print('Leap year')
else:
    print('Not leap year')
