import random
import requests


def random_pokemon():
    pokemon_number = random.randint(1, 898)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'hp': pokemon['stats'][0]['base_stat'],
        'attack': pokemon['stats'][1]['base_stat'],
        'defense': pokemon['stats'][2]['base_stat'],
        'special attack': pokemon['stats'][3]['base_stat'],
        'special defense': pokemon['stats'][4]['base_stat'],
        'speed': pokemon['stats'][5]['base_stat'],
    }


f = open('battle.txt', 'w+')
f.write('A wild Pokemon has appeared! \n')
f.close()


def run():
    no_of_rounds = int(input('How many rounds do you want to play? '))
    for game_rounds in range(no_of_rounds):
        print('A wild Pokemon has appeared!')
        my_pokemon_1 = random_pokemon()
        my_pokemon_2 = random_pokemon()
        my_pokemon_3 = random_pokemon()
        print('You have the following Pokemon in your party:')
        print('Pokemon 1: {}'.format(my_pokemon_1['name'].title()))
        print('Pokemon 2: {}'.format(my_pokemon_2['name'].title()))
        print('Pokemon 3: {}'.format(my_pokemon_3['name'].title()))
        fighting_pokemon = input(
            'Which Pokemon would you like to choose? (Pick: 1, 2, or 3) ')
        if fighting_pokemon == '1':
            print('{}, I choose you! '.format(my_pokemon_1['name'].title()))
            fighting_pokemon = my_pokemon_1
            f = open('battle.txt', 'a+')
            f.write('You chose to fight with {}! '.format(
                my_pokemon_1['name'].title()))
            f.close()
        elif fighting_pokemon == '2':
            print('{}, I choose you! '.format(my_pokemon_2['name'].title()))
            fighting_pokemon = my_pokemon_2
            f = open('battle.txt', 'a+')
            f.write('You chose to fight with {}! '.format(
                my_pokemon_2['name'].title()))
            f.close()
        elif fighting_pokemon == '3':
            print('{}, I choose you!'.format(my_pokemon_3['name'].title()))
            fighting_pokemon = my_pokemon_3
            f = open('battle.txt', 'a+')
            f.write('You chose to fight with {}! '.format(
                my_pokemon_3['name'].title()))
            f.close()
        stat_choice = input(
            'Which stat do you want to use? \n (hp, attack, defense, special attack, special defense, speed) '
        )
        opponent_pokemon = random_pokemon()
        print('The wild Pokemon is {}'.format(
            opponent_pokemon['name'].title()))
        f = open('battle.txt', 'a+')
        f.write('You fought against {}! '.format(
            opponent_pokemon['name'].title()))
        f.close()
        my_stat = (fighting_pokemon[stat_choice])
        print(f'Your Pokemon\'s stat is {my_stat}')
        opponent_stat = opponent_pokemon[stat_choice]
        print(f'The opposing Pokemon\'s stat is {opponent_stat}')
        if my_stat > opponent_stat:
            print(
                'Yay!! Your Pokemon has won! You throw a Pokeball and capture the wild Pokemon! \n'
            )
            f = open('battle.txt', 'a+')
            f.write('You won! \n')
            f.close()
        elif my_stat < opponent_stat:
            print(
                'Oh no!! Your Pokemon was defeated! The wild Pokemon escapes! \n'
            )
            f = open('battle.txt', 'a+')
            f.write('You lost! \n')
            f.close()
        else:
            print('Your Pokemon and the wild Pokemon are at a stalemate! \n')
            f = open('battle.txt', 'a+')
            f.write('It was a draw! \n')
            f.close()


run()
