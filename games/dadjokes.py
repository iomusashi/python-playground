"""
dadjokes: Acquire instant dad jokes on your terminal. (Internet required)

Purpose:
A simple RESTful API consumption using python.

Requirements:
pip install requests, pyfiglet, termcolor

Working on a venv is recommended.
"""
import pyfiglet
import requests

from random import choice
from termcolor import colored

figlet = pyfiglet.figlet_format('DAD JOKES')
welcome = colored(figlet, color='cyan')
print(welcome)

base_url = 'https://icanhazdadjoke.com'
endpoint = '/search'
url = f'{base_url}{endpoint}'

print('Heya, kiddo!')
user_input = input('What topic would you like to hear about? ')
response = requests.get(url,
                        headers={
                            'Accept': 'application/json'
                        },
                        params={
                            'term': user_input
                        })
json = response.json()
total_jokes = json['total_jokes']
results = json['results']
if total_jokes > 1:
    print(f'I have {total_jokes} jokes about {user_input}, here\'s one:')
    print(choice(results)['joke'])
elif total_jokes == 1:
    print(f'I have one joke about {user_input}, here\'s one:')
    print(results[0]['joke'])
else:
    print(f'Nope, can\'t do a {user_input} joke.')
