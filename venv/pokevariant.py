import random

import requests

def random_pokemon():
    pokemon_number = random.randint(1, 898)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

def run():
  no_of_rounds=int(input('How many rounds do you want to play? '))
  for game_rounds in range(no_of_rounds):
    print('A wild Pokemon has been spotted!')
    my_pokemon_1 = random_pokemon()
    my_pokemon_2 = random_pokemon()
    my_pokemon_3 = random_pokemon()

    print('You have the following Pokemon in your party:')
    print('Pokemon 1: {}'.format(my_pokemon_1['name'].title()))
    print('Pokemon 2: {}'.format(my_pokemon_2['name'].title()))
    print('Pokemon 3: {}'.format(my_pokemon_3['name'].title()))

    fighting_pokemon = input('Which Pokemon would you like to choose? (Pick: 1, 2, or 3) ')
        if fighting_pokemon == 1:
            print('You have chosen to fight with {}'.format(my_pokemon_1['name'].title()))
        if fighting_pokemon == 2:
            print('You have chosen to fight with {}'.format(my_pokemon_2['name'].title()))
        if fighting_pokemon == 3:
            print('You have chosen to fight with {}'.format(my_pokemon_3['name'].title()))

    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    opponent_pokemon = random_pokemon()
    print('The wild Pokemon is {}'.format(opponent_pokemon['name'].title()))
    my_stat = fighting_pokemon[stat_choice]
    print(f'Your Pokemon\'s stat is {my_stat}')
    opponent_stat = opponent_pokemon[stat_choice]
    print(f'The opposing Pokemon\'s stat is {opponent_stat}')
    if my_stat > opponent_stat:
      print('Your Pokemon has won!')
    elif my_stat < opponent_stat:
      print('Your Pokemon was defeated!')
    else:
      print('Your Pokemon and the wild Pokemon are at a stalemate!')
run()
