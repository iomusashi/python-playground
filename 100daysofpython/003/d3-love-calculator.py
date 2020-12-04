print('Welcome to the Love Calculator!')

def countFor(character, name1, name2):
    count = name1.lower().count(character) + name2.lower().count(character)
    print(f'{character} occurs {count} times')
    return count

name1 = input('What is your name? ')
name2 = input('What is their name? ')

t_count = countFor('t', name1, name2)
r_count = countFor('r', name1, name2)
u_count = countFor('u', name1, name2)
e_count = countFor('e', name1, name2)

true_count = t_count + r_count + u_count + e_count
print(f'Total = {true_count}')

l_count = countFor('l', name1, name2)
o_count = countFor('o', name1, name2)
v_count = countFor('v', name1, name2)

love_count = l_count + o_count + v_count + e_count
print(f'Total = {love_count}')

total_score = int(f'{true_count}{love_count}')

if total_score < 10 or total_score > 90:
    print(f'Your score is {total_score}, you go together like coke and mentos.')
elif total_score >= 40 and total_score <= 50:
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}')
