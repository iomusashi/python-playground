from os import name
from os import system


def clear():
    system('cls' if name == 'nt' else 'clear')
