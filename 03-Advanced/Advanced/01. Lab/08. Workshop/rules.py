def rules(mx, busy_positions):
    def horizontal(mx):
        for i in range(len(mx)):
            marks = list()
            for j in range(len(mx[0])):
                if mx[i][j] != ' ':
                    marks.append(mx[i][j])
            if check_if_won(marks) is not None:
                return check_if_won(marks)

    def vertical(mx):
        for j in range(len(mx[0])):
            marks = list()
            for i in range(len(mx)):
                if mx[i][j] != ' ':
                    marks.append(mx[i][j])
            if check_if_won(marks) is not None:
                return check_if_won(marks)

    def diagonal1(mx):
        i, j = 0, 0
        while i < len(mx):
            marks = list()
            while j < len(mx[0]):
                if mx[i][j] != ' ':
                    marks.append(mx[i][j])
                i += 1
                j += 1
            if check_if_won(marks) is not None:
                return check_if_won(marks)

    def diagonal2(mx):
        i, j = 0, len(mx[0]) - 1
        while i < len(mx) - 1:
            marks = list()
            while j != -1:
                if mx[i][j] != ' ':
                    marks.append(mx[i][j])
                i += 1
                j -= 1
            if check_if_won(marks) is not None:
                return check_if_won(marks)

    if len(busy_positions) == 9:
        return 'Draw!'
    vertical(mx)
    rules_list = [horizontal(mx), vertical(mx), diagonal1(mx), diagonal2(mx)]
    for element in rules_list:
        if element is not None:
            return element


def check_if_won(iterable):
    if len(iterable) == 3:
        iterable = set(iterable)
        if len(iterable) == 1:
            return iterable.pop()