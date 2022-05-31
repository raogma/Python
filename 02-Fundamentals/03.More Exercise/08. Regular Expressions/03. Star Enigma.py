from re import finditer


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


def fill(iterable: dict, element):
    for key in iterable:
        if iterable[key] == element[0]:
            if '-' in element:
                iterable[key] = int(element[2:])
            elif '!' in element:
                iterable[key] = element[1:-1]
            elif '@' in element:
                element = ''.join([x for x in element if x.isalpha()])
                iterable[key] = element
            else:
                element = element[1:]
                if element.isdigit():
                    element = int(element)
                iterable[key] = element
            break


key = list('star')
regex = r'(@[A-Za-z]+[^@\-!:>]*)|(:\d+[^@\-!:>]*)|(![A|D]![^@\-!:>]*)|(->\d+)'
planet_data = {
    'A': [],
    'D': [],
}

for _ in range(int(input())):
    data = {
        'planet': '@',
        'population': ':',
        'attack_type': '!',
        'soldiers_count': '-',
    }
    line = input()
    line = decrypt(key, line)
    fill_counter = 0

    for element in finditer(regex, line):
        element = element.group()
        fill(data, element)
        fill_counter += 1

    if fill_counter == 4:
        if data['planet'] not in planet_data[data['attack_type']]:
            planet_data[data['attack_type']].append(data['planet'])

print(printing(planet_data))