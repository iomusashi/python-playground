def is_leap(year):
    is_divisible_by_4 = year % 4 == 0
    not_divisible_by_100 = year % 100 != 0
    is_divisible_by_400 = year % 400 == 0
    return is_divisible_by_4 and (not_divisible_by_100 or is_divisible_by_400)


def days_in_month(year, month):
    month_days = [31, 28 if not is_leap(
        year) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]


year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
print(days_in_month(year, month))
