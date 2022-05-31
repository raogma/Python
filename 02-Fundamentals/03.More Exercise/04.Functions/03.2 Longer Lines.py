from math import floor


def center(tuple1, tuple2):
    distance_A = tuple1[0] ** 2 + tuple1[1] ** 2
    distance_B = tuple2[0] ** 2 + tuple2[1] ** 2

    if distance_A > distance_B:
        return tuple2, tuple1
    else:
        return tuple1, tuple2

    
a = tuple(float(input()) for _ in range(2))
b = tuple(float(input()) for _ in range(2))
c = tuple(float(input()) for _ in range(2))
d = tuple(float(input()) for _ in range(2))

x1 = a[0] + b[0]
y1 = a[1] + b[1]
x2 = c[0] + d[0]
y2 = c[1] + d[1]

first_distance = x1 ** 2 + y1 ** 2
second_distance = x2 ** 2 + y2 ** 2

if first_distance >= second_distance:
    print(''.join(map(str, center(tuple(map(floor, a)), tuple(map(floor, b))))))
else:
    print(''.join(map(str, center(tuple(map(floor, c)), tuple(map(floor, d))))))