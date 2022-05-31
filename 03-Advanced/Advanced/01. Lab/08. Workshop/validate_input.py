from re import findall
from collections import OrderedDict, deque


def validate_symbol(dictionary, iterable, person):
    if len(iterable) == 2:
        symbol = input(f'{person} would you like to play with \'X\' or \'O\'? ')
        if symbol in iterable:
            dictionary[person] = iterable.pop(iterable.index(symbol))
            validate_symbol(dictionary, iterable, person)
        else:
            print('Invalid Symbol! Try again!')
            validate_symbol(dictionary, iterable, person)
    else:
        for person in dictionary:
            if dictionary[person] is None:
                dictionary[person] = iterable.pop()
        return


def validate_position(busy_positions, player):
    position = input(f'{player} choose a free position [1-9]: ')
    if position.isdecimal():
        if 0 < int(position) < 10:
            if position not in busy_positions:
                return position
            else:
                print('Position already taken! Try again!')
        else:
            print('Position out of range! Try again!')
    else:
        print('Invalid position! Try again!')
    return validate_position(busy_positions, player)


def validate_player_name(players_msg, re, dictionary):
    player = input(players_msg)
    match = findall(re, player)
    if len(''.join(match)) == len(player):
        dictionary[player] = None
        return
    else:
        print('Invalid Name!')
        validate_player_name(players_msg, re, dictionary)


def get_player_info():
    regex = r'[a-zA-Z]+[\w]+'
    info = OrderedDict()
    symbols = ['X', 'O']
    players_msg = deque(['Player one name: ', 'Player two name: '])
    for msg in players_msg:
        validate_player_name(msg, regex, info)

    for player in info:
        validate_symbol(info, symbols, player)
    return info
