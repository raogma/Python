from math import floor


def center(tuple1, tuple2):
    distance_A = tuple1[0] ** 2 + tuple1[1] ** 2
    distance_B = tuple2[0] ** 2 + tuple2[1] ** 2

    info = {
        distance_A > distance_B: tuple(map(floor, tuple2)),
        distance_A <= distance_B: tuple(map(floor, tuple1)),
    }

    for key in info:
        if key:
            return info[key]


A = tuple(float(input()) for _ in range(2))
B = tuple(float(input()) for _ in range(2))

print(center(A, B))
