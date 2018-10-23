"""
jan-ken-pon:
jak-en-poy or batobatopik in the PH

A rock-paper-scissors game in terminal.

Purpose:
Test if python functions are hoisted or not.

Findings:
Python functions are not hoisted:
functions are required to be defined first before use.
"""
import random

# 0-rock, 1-paper, 2-scissors
random_number = random.randint(0, 2)
player_pick = None
computer_pick = None

def stringify(random_number):
    """Returns the string representation of the pick.
    0: Rock,
    1: Paper,
    2: Scissors
    """
    if random_number == 0:
        return "rock"

    elif random_number == 1:
        return "paper"

    else:
        return "scissors"

def printResult(player_pick, computer_pick):
    """
    Prints the result for player vs computer picks.
    """
    print(f'Player plays {player_pick}')
    print(f'Computer plays {computer_pick}')

    if player_pick == computer_pick:
        print('It\'s a tie!')

    elif player_pick == "rock":
        if computer_pick == 'scissors':
            print('You win!')
        else:
            print('You lose!')

    elif player_pick == 'paper':
        if computer_pick == 'rock':
            print('You win!')
        else:
            print('You lose!')

    elif player_pick == 'scissors':
        if computer_pick == 'paper':
            print('You win!')
        else:
            print('You lose!')
    else:
        print(f'LOL wut\'s a {player_pick}?')

while True:
    print('-----------------------------------')
    print("Rock, paper, or scissors.")
    player_pick = input('What\'s your play? ').lower()
    computer_pick = stringify(random_number)
    print('-----------------------------------')
    printResult(player_pick = player_pick,
                computer_pick = computer_pick)
    print('-----------------------------------')
    play_again = input('Do you want to play again? (y/n) ')

    if play_again == 'y':
        random_number = random.randint(0, 2)
        player_pick = None
        computer_pick = None

    else:
        print('Thank you for playing')
        print('Game Over')
        break
