from collections import OrderedDict


def fill(iterable: dict, color, name, dmg, hp, armor):
    if color not in iterable:
        iterable[color] = {}
    iterable[color][name] = [dmg, hp, armor]


data = OrderedDict()

for _ in range(int(input())):
    color, name, dmg, hp, armor = input().split()
    dmg, hp, armor = map(int, (dmg, hp, armor))
    fill(data, color, name, dmg, hp, armor)

data = dict(sorted(data.items()))