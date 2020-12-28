import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

jankenpon = [rock, paper, scissors]

choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n'))

if choice < 0 or choice > len(jankenpon) - 1:
    print('Invalid choice')
    raise SystemExit(0)

print(jankenpon[choice])

print('Computer chose:')
computer_choice = random.randint(0, len(jankenpon) - 1)
print(jankenpon[computer_choice])

if choice == 0 and computer_choice == 2:
    print('You win!')
elif computer_choice == 0 and choice == 2:
    print('You lose!')
elif choice > computer_choice:
    print('You win!')
elif computer_choice > choice:
    print('You lose!')
else:
    print('Draw!')
