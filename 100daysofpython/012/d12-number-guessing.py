from random import randint

print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
def generate_random_number():
  return randint(1, 101)

def acquire_guess():
  print(f'You have {attempts} {"attempts" if attempts > 1 else "attempt"} remaining to guess the number.')
  return int(input('Make a guess: '))

def compare(guess, answer):
  if guess > answer:
    print('Too high.')
  elif guess < answer:
    print('Too low.')
  else:
    print(f'You guessed it right! The number is {answer}.')
    raise SystemExit()

answer = generate_random_number()
guess = 0
difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
attempts = 10 if difficulty == 'easy' else 5

while attempts > 0 and answer != guess:
  guess = acquire_guess()
  compare(guess, answer)
  attempts -= 1

print(f'You failed to guess {answer}')
