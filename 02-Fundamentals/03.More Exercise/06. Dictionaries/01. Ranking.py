def printing(iterable):
    res = str()
    name = find_best_candidate(sum_points(iterable))[0]
    total = find_best_candidate(sum_points(iterable))[1]
    res += f'Best candidate is {name} with total {total} points.\nRanking:\n'
    for key in sorted(iterable):
        res += f'{key}\n'
        for sub_key in sorted(iterable[key].items(), key=lambda el: el[1], reverse=True):
            res += f'#  {sub_key[0]} -> {sub_key[1]}\n'
    return res


def sum_points(iterable):
    sum_points = {}
    for key in iterable:
        sum = 0
        for sub_key in iterable[key]:
            sum += iterable[key][sub_key]
        sum_points[key] = sum
    return sum_points


def find_best_candidate(iterable):
    points = 0
    for key in iterable:
         if iterable[key] > points:
             points = iterable[key]
             save_key = key
    return save_key, points


data = {}
while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    data[contest] = password

users = {}
while True:
    command = input()
    if command == 'end of submissions':
        break
    contest, password, username, points = command.split('=>')
    if contest in data:
        if password == data[contest]:
            if username not in users:   # add new person
                users[username] = {}
            if contest in users[username]:
                if int(points) > users[username][contest]: # update the points only if the new ones are more than...
                    users[username][contest] = int(points)
            else:
                users[username][contest] = int(points)

print(printing(users)[:-1])
