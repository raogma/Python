INCREASE = 1
DECREASE = -1
RESULT = str()


def print_rhombus(i, direction, count):
    i += direction
    if i == 0:
        return
    if i == count:
        direction = DECREASE
    global RESULT
    RESULT += ' ' * (count - i) + '* ' * i + '\n'
    print_rhombus(i, direction, count)


print_rhombus(0, INCREASE, int(input()))
print(RESULT)