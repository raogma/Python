from re import findall


def printing(iterable: dict):
    res = str()
    for key in dict(sorted(iterable.items(), key=lambda x: x[0])):
        if key == 'A':
            res += f'Attacked planets: {len(iterable[key])}\n'
        else:
            res += f'Destroyed planets: {len(iterable[key])}\n'
        for subkey in list(sorted(iterable[key])):
            res += f'-> {subkey}\n'
    return res


def decrypt(key, line):
    def find_count(key, line):
        count = 0
        for symbol in line.lower():
            if symbol in key:
                count += 1
        return count

    count = find_count(key, line)
    line = list(map(ord, line))
    line = [line[i] - count for i in range(len(line))]
    return ''.join(list(map(chr, line)))


key = list('star')
planet_data = {
    'A': [],
    'D': [],
}

for _ in range(int(input())):
    line = input()
    line = decrypt(key, line)

    planet = findall(r'@[A-Za-z]+[^@\-!:>]*', line)
    if not planet:
        continue
    population = findall(r':\d+[^@\-!:>]*', line)
    if not population:
        continue
    attack_type = findall(r'![A|D]![^@\-!:>]*', line)
    if not attack_type:
        continue
    soldiers = findall(r'->\d+', line)
    if not soldiers:
        continue

    planet = ''.join([x for x in ''.join(planet) if x.isalpha()])
    attack_type = ''.join(attack_type)[1:-1]

    ####
    planet_data[attack_type].append(planet)

print(printing(planet_data))