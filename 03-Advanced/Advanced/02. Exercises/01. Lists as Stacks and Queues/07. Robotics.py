from collections import deque


def distribute_robots(info: dict, avlbl: list, raw_data: input):
    for element in raw_data:
        rbt, tm = element.split('-')
        info[rbt] = int(tm)
        avlbl.append(rbt)


def distribute_products(prdcts: list):
    while True:
        line = input()
        if line == 'End':
            break
        else:
            prdcts.append(line)


def get_time(total_s):
    h = total_s // 60 // 60
    if h > 23:
        h = 0
    m = total_s // 60 % 60
    s = total_s % 60
    return f'{h:02d}:{m:02d}:{s:02d}'


robot_data = input().split(';')
hours, minutes, seconds = list(map(lambda x: int(x), input().split(':')))

robot_info = dict()
available, unavailable, products = deque(), list(), deque()
distribute_robots(robot_info, available, robot_data)
distribute_products(products)
starting_time = hours * 60 * 60 + minutes * 60 + seconds
total_seconds = starting_time

while products:
    product = products.popleft()
    total_seconds += 1
    if unavailable:                                    # when busy time of robot is over
        i = 0
        while not i >= len(unavailable):
            robot, time_left = unavailable[i]           # time_left == unavailable[i][1]
            if unavailable[i][1] - 1 > 0:
                unavailable[i][1] -= 1
            else:
                available.append(robot)
                unavailable.pop(i)
            i += 1
    if available:                                   # if there are av robots to work on the product
        robot = available.popleft()
        unavailable.append([robot, robot_info[robot]])
        print(f'{robot} - {product} [{get_time(total_seconds)}]')
    else:
        products.append(product)
