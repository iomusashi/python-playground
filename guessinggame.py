'''
Game randomly picks a number in the range of 1-10.

Player needs to guess correctly to beat the game.
'''

import random

random_number = random.randint(1, 10)
guess = None
trials = 0

while trials < 5:
  '''
  Gameover scenario: Player failed to guess after 5 trials.
  '''
  guess = input('Pick a number from 1 to 10: ')
  guess = int(guess) # Force parse to int

  if guess < random_number:
    print('Incorrect - Pick higher.')
    trials += 1

  elif guess > random_number:
    print('Incorrect - Pick lower.')
    trials += 1

  else:
    print('CORRECT!')
    play_again = input('Do you want to play again? (y/n) ')
    if play_again == 'y':
      random_number = random.randint(1, 10)
      guess = None
      trials = 0
    else:
      print('Thank you for playing')
      break

print('Game Over')