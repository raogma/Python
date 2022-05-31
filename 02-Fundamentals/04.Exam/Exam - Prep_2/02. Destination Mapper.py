from re import finditer


def printing(iterable: list, value):
    res = 'Destinations: '
    res += f"{', '.join(iterable)}\nTravel Points: {value}"
    return res


regex = r'([=|/])[A-Z][a-zA-Z][a-zA-Z]+\1'
destinations = []
points = 0
for element in finditer(regex, input()):
    destination = element.group()
    destination = destination[1: len(destination) - 1]
    destinations.append(destination)
    points += len(destination)

print(printing(destinations, points))
