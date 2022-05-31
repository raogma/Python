from math import floor, sqrt
from sys import maxsize


def center(tuple1, tuple2):
    distance_A = sqrt(tuple1[0] ** 2 + tuple1[1] ** 2)
    distance_B = sqrt(tuple2[0] ** 2 + tuple2[1] ** 2)

    if distance_A > distance_B:
        return tuple2, tuple1
    elif distance_A == distance_B:
        return tuple1, tuple2
    else:
        return tuple1, tuple2


info = []
points = {}

for _ in range(4):
    info.append(tuple(float(input()) for _ in range(2)))

for i in range(0, len(info), 2):
    first_side = info[i][0] + info[i + 1][0]
    second_side = info[i][1] + info[i + 1][1]
    distance = sqrt(first_side ** 2 + second_side ** 2)
    points[distance] = [tuple(map(floor, info[i])), tuple(map(floor, info[i + 1]))]

max_distance = -maxsize

for key in points:
    if key > max_distance:
        max_distance = key

print(''.join(map(str, center(points[max_distance][0], points[max_distance][1]))))