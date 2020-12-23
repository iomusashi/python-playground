from d14_higherlower_art import logo
from d14_higherlower_art import vs
from d14_higherlower_gamedata import data
from d14_higherlower_utils import clear

from random import choice

pick1 = {}
pick2 = {}
score = 0

def initialize():
  global pick1
  global pick2
  global score
  pick1 = choice(data)
  pick2 = pick1
  score = 0

def higherlower():
  global pick1
  global pick2
  global score

  in_play = True
  while in_play:
    while pick2 == pick1:
      pick2 = choice(data)
    
    clear()
    print(logo)
    if score > 0:
      print(f"You're right! Current score: {score}")
    print(f"Compare A: {pick1['name']}, a {pick1['description']}, from {pick1['country']}")
    print(vs)
    print(f"Against B: {pick2['name']}, a {pick2['description']}, from {pick2['country']}")
    player_pick = input('Who has more followers? Type \'A\' or \'B\': ').lower()
    if int(pick1['follower_count']) > int(pick2['follower_count']) and player_pick == 'a':
      pick1 = pick2
      score += 1
    elif int(pick2['follower_count']) > int(pick1['follower_count']) and player_pick == 'b':
      pick1 = pick2
      score += 1
    else:
      clear()
      print(logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      in_play = False

initialize()
higherlower()
