"""
TwoFace - Harvey Dent

Riddler:
Hello, Dark Knight.
Imagine Harvey Dent (TwoFace) pointing a gun at your face.
Will you live or will you die?

Find out your odds in this simulator game.
"""
import random as rnd

def coinflip():
    """Returns either 'heads' or 'tails'"""
    odds = rnd.random() # Generates a number between 0 and 1.
    if odds > 0.5:
        return 'heads'
    else:
        return 'tails'

def verdict(coin, choice):
    if coin == choice:
        print('Harvey: "Congratulations Dark Knight.')
        print('Harvey: "You\'ll live to fight another day."')
        print('VERDICT: You LIVED')
    else:
        print('Harvey: "Ain\'t so lucky now eh, Dark Knight?"')
        print('Harvey: *Shoots the gun.')
        print('VERDICT: You DIED')

player_pick = None

while True:
    print('-----------------------------------')
    print('Harvey: "Alright, Dark Knight. Time to choose."')
    print('Harvey: "Heads or tails?"')
    player_pick = input('Dark Knight: ').lower()
    print('-----------------------------------')
    print('Harvey: *Flips the coin*')
    coin = coinflip()
    verdict(coin = coin,
            choice = player_pick)
    print('-----------------------------------')
    play_again = input('Do you want to want to play again? (y/n) ')

    if play_again == 'y':
        player_pick = None
    else:
        print('Thank you for playing')
        print('Game Over')
        break
