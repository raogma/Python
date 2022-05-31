GROWING = 1
SHRINKING = -1


def rhombus(count):
    def print_line(i, direction):
        print(' ' * (count - i) + '* ' * i)
        if i == 0:
            return
        if i == count:
            direction = SHRINKING
        print_line(i + direction, direction)
    print_line(1, GROWING)


rhombus(int(input()))