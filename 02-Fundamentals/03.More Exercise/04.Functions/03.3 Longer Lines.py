from math import sqrt, floor


def center(tuple1, tuple2):
    distance_A = sqrt(tuple1[0] ** 2 + tuple1[1] ** 2)
    distance_B = sqrt(tuple2[0] ** 2 + tuple2[1] ** 2)

    if distance_A > distance_B:
        return tuple2, tuple1
    else:
        return tuple1, tuple2


a = tuple(float(input()) for _ in range(2))
b = tuple(float(input()) for _ in range(2))
c = tuple(float(input()) for _ in range(2))
d = tuple(float(input()) for _ in range(2))

first_side = a[0] + b[0]
second_side = a[1] + b[1]
third_side = c[0] + d[0]
forth_side = c[1] + d[1]

first_distance = sqrt(first_side ** 2 + second_side ** 2)
second_distance = sqrt(third_side ** 2 + forth_side ** 2)

if first_distance > second_distance:
    print(''.join(map(str, center(tuple(map(floor, a)), tuple(map(floor, b))))))
else:
    print(''.join(map(str, center(tuple(map(floor, c)), tuple(map(floor, d))))))