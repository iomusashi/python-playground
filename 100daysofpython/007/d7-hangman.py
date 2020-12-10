import random

word_list = ['aardvark', 'baboon', 'camel']

answer = random.choice(word_list)
print(f'psst. the chosen word is {answer}')

letters = []
for c in answer:
    letters.append('_')
print(letters)

word_guessed = ''.join(letters)
while word_guessed != answer:
    guess = input('Guess a letter: ')
    for i in range(0, len(answer)):
        c = answer[i]
        if guess == c:
            letters[i] = c
    word_guessed = ''.join(letters)
    print(letters)

print('Omedeto!')
