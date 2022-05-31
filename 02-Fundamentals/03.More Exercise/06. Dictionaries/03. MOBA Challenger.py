from sys import maxsize


def calculate_points(iterable):
    score = {}
    for key in iterable:
        total = 0
        for subkey in iterable[key]:
            total += iterable[key][subkey]
        score[key] = total
    return score


def find_loser(iterable, *names):
    min_points = maxsize
    for name in names:
        if iterable[name] < min_points:
            min_points = iterable[name]
            save_name = name
        elif iterable[name] == min_points:
            return
    return save_name


def printing(iterable):
    res = str()
    total_points = calculate_points(iterable)
    for key in dict(sorted(total_points.items(), key=lambda el: (-el[1], el[0]))):
        res += f'{key}: {total_points[key]} skill\n'
        for subkey in dict(sorted(iterable[key].items(), key=lambda el: (-el[1], el[0]))):
            res += f'- {subkey} <::> {iterable[key][subkey]}\n'
    return res


player_pool = dict()
while True:
    command = input()
    if command == 'Season end':
        break
    if '->' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)

        if player not in player_pool:
            player_pool[player] = {}

        if position in player_pool[player]:
            if skill > player_pool[player][position]:
                player_pool[player][position] = skill
        else:
            player_pool[player][position] = skill

    else:
        player1, player2 = command.split(' vs ')
        if player1 in player_pool and player2 in player_pool:
            if player_pool[player1].keys() & player_pool[player2].keys():  # check if position in common
                if find_loser(calculate_points(player_pool), player1, player2) is not None:  # check equal points
                    lost_player = find_loser(calculate_points(player_pool), player1, player2)
                    del player_pool[lost_player]

print(printing(player_pool))