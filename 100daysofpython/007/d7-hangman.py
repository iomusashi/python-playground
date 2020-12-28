import random
from d7_hangman_art import stages
from d7_hangman_word import word_list

answer = random.choice(word_list)
lives = len(stages) - 1

letters = []
for c in answer:
    letters.append('_')
print(letters)
print(stages[lives])

word_guessed = ''.join(letters)
while word_guessed != answer and lives > 0:
    guess = input('Guess a letter: ')
    if not guess in answer:
        lives -= 1
    for i in range(0, len(answer)):
        c = answer[i]
        if guess == c:
            letters[i] = c
    word_guessed = ''.join(letters)
    print(letters)
    print(stages[lives])

if lives > 0:
    print('Congratulations! You won!')
else:
    print(f'You\'ve been hanged! The word is {answer}.')
print('Game over!')
