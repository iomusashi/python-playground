from os import name
from os import system
from d8_blind_auction_art import logo


def clear():
    system('cls' if name == 'nt' else 'clear')


participants = {}

clear()
print(logo)
print('Welcome to the secret auction program.')
participant = input('What is your name? ')
bid = int(input('What\'s your bid? $'))
participants[participant] = bid
has_more_bidders = input(
    'Are there any other bidders? Type \'yes\' or \'no\'.\n') == 'yes'

while has_more_bidders:
    clear()
    participant = input('What is your name? ')
    bid = int(input('What\'s your bid? $'))
    participants[participant] = bid
    has_more_bidders = input(
        'Are there any other bidders? Type \'yes\' or \'no\'.\n') == 'yes'

clear()
winner = None
top_bid = 0
for participant in participants:
    if participants[participant] > top_bid:
        winner = participant
        top_bid = participants[participant]

print(f'The winner of the bid is {winner} with a bid of ${top_bid}.')
