from itertools import permutations


def possible_permutations(iterable: list):
    for p in permutations(iterable):
        yield list(p)


[print(n) for n in possible_permutations([1, 2, 3])]