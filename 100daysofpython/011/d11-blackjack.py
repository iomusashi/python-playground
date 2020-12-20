from functools import reduce
from random import choice

from d11_blackjack_art import logo
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

def count_ace(draw):
  return draw.count('Ace')

def is_bust_or_blackjack(draw):
  return calculate_score(draw) >= BLACKJACK

def calculate_score(draw):
  value_map = list(map(lambda card: card_score[card], draw))
  score = reduce(lambda x, y: x + y, value_map, 0)
  return score if score <= BLACKJACK else score - (10 * count_ace(draw))

def compare(player_score, computer_score):
  if player_score > BLACKJACK:
    print('You have a bust! You lose!')
  elif computer_score > BLACKJACK:
    print('Computer went over. You win!')
  elif player_score == computer_score:
    print('Draw!')
  elif player_score > computer_score:
    print('You win!')
  else:
    print('You lose!')

def check_for_blackjack(player, computer):
  player_is_blackjack = has_blackjack(player)
  computer_is_blackjack = has_blackjack(computer)

  if player_is_blackjack and computer_is_blackjack:
    print(f'Computer: {", ".join(card for card in computer)}')
    print(f'Player: {", ".join(card for card in player)}')
    print('Draw! You both have a blackjack!')
  elif computer_is_blackjack:
    print(f'Computer: {", ".join(card for card in computer)}')
    print('The computer drawed a blackjack. You lose!')
    print('Game over.')
  elif player_is_blackjack:
    print(f'Player: {", ".join(card for card in player)}')
    print('You drawed a blackjack! You win!')
    print('Congratulations!')

def blackjack():
  clear()
  print(logo)
  player_score = 0
  computer_score = 0

  player = [deal_card(), deal_card()]
  computer = [deal_card(), deal_card()]

  check_for_blackjack(player, computer)

  player_round = True
  while player_round:
    player_score = calculate_score(player)
    print(f'Player: {", ".join(card for card in player)}')
    print(f'Your current score: {player_score}')
    print('')
    print(f'Computer: {computer[0]}')
    if not is_bust_or_blackjack(player):
      player_deal_more = input('Type \'y\' to get another card, type \'n\' to pass: ').lower() == 'y'
      if player_deal_more:
        player.append(deal_card())
      else:
        player_round = False
    else:
      player_round = False

  computer_score = calculate_score(computer)
  while computer_score < 17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)

  print(f'Your final hand: {", ".join(card for card in player)}')
  print(f'Computers final hand: {", ".join(card for card in computer)}')
  print('')
  print(f'Your final score: {player_score}')
  print(f'Computer final score: {computer_score}')
  compare(player_score, computer_score)

while input('Do you want to play a game of Blackjack? Type \'y\' or \'n\': ').lower() == 'y':
  blackjack()
