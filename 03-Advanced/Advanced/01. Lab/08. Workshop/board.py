def create_board():
    mx = [[' '] * 3 for _ in range(3)]
    return mx


def enumerate_board(mx):
    n = 0
    for element in mx:
        for i in range(len(element)):
            n += 1
            element[i] = n
    return mx


def get_state_of_board(mx):
    res = str()
    for i in range(len(mx)):
        for j in range(len(mx)):
            res += '|'
            if mx[i][j]:
                res += ' ' + str(mx[i][j]) + ' '
            else:
                res += '   '

            if j == len(mx[i]) - 1:
                if i == len(mx) - 1 and j == (len(mx[i]) - 1):
                    res += '|'
                else:
                    res += '|\n'
    return res
