import random

names_string = input('Give me everybody\'s names, separated by a comma.\n')
names = names_string.split(', ')

member_count = len(names)

picked_index = random.randint(0, member_count - 1)
print(f'{names[picked_index]} is going to buy the meal today!')
