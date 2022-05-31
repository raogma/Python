INCREASE = 1
DECREASE = -1


def print_rhombus(i, direction, count, res):
    i += direction
    if i == 0:
        print(res)
        return
    if i == count:
        direction = DECREASE
    res += ' ' * (count - i) + '* ' * i + '\n'
    print_rhombus(i, direction, count, res)


print_rhombus(0, INCREASE, int(input()), str())