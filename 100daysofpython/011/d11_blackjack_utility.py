from os import name
from os import system

BLACKJACK = 21


def clear():
    system('cls' if name == 'nt' else 'clear')
