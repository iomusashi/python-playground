alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n')
if direction != 'encode' and direction != 'decode':
  raise SystemExit(0)

text = input(f'Type your message to {direction}:\n').lower()
shift = int(input('Type the shift number:\n'))

def encrypt(text, shift):
  cipher_text = ''
  for char in text:
    index = alphabet.index(char)
    shifted = index + shift
    shifted = shifted if shifted < len(alphabet) else shifted % len(alphabet)
    letter = alphabet[shifted]
    cipher_text += letter
  print(f'The encoded text is {cipher_text}')

def decrypt(cipher_text, shift):
  text = ''
  for char in cipher_text:
    index = alphabet.index(char)
    shifted = index - shift
    letter = alphabet[shifted]
    text += letter
  print(f'The decoded cipher text is {text}')

if direction == 'encode':
  encrypt(text, shift)
elif direction == 'decode':
  decrypt(text, shift)
else:
  raise SystemExit(0)
