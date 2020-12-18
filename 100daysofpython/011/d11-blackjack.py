from functools import reduce
from random import choice

from d11_blackjack_utility import clear
from d11_blackjack_utility import BLACKJACK
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King']
card_score = {
  'Ace': 11,
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'Jack': 10,
  'Queen': 10,
  'King': 10
}
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def deal_card():
  return choice(cards)

def has_blackjack(draw):
  return calculate_score(draw) == BLACKJACK

def calculate_score(draw):
  value_map = list(map(lambda card: card_score, draw))
  return reduce(lambda x, y: x + y, value_map, 0)

# play = True
# while play:

clear()
player = [deal_card(), deal_card()]
computer = [deal_card(), deal_card()]
print(f'player: {player}')
print(f'computer: {computer}')

player_is_blackjack = has_blackjack(player)
computer_is_blackjack = has_blackjack(computer)

if computer_is_blackjack:
  print('The computer drawed a blackjack. You lose!')
  print('Game over.')
elif player_is_blackjack:
  print('You drawed a blackjack! You win!')
  print('Congratulations!')
else:
  player_score = calculate_score(player)
  computer_score = calculate_score(computer)