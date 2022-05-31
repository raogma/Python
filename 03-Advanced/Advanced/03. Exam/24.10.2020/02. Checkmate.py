QUEENS = []


def find_king(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'K':
                return i, j


def queens_collision(board):
    x, y = find_king(board)
    # right
    for j in range(y + 1, len(board[0])):
        if board[x][j] == 'Q':
            QUEENS.append([x, j])
            break
    # left
    for j in range(y - 1, -1, -1):
        if board[x][j] == 'Q':
            QUEENS.append([x, j])
            break

    # up
    for i in range(x + 1, len(board)):
        if board[i][y] == 'Q':
            QUEENS.append([i, y])
            break

    # down
    for i in range(x - 1, -1, -1):
        if board[i][y] == 'Q':
            QUEENS.append([i, y])
            break

    # up right
    for i, j in zip(range(x - 1, -1, -1), range(y + 1, len(board[0]))):
        if board[i][j] == 'Q':
            QUEENS.append([i, j])
            break

    # down right
    for i, j in zip(range(x + 1, len(board)), range(y + 1, len(board[0]))):
        if board[i][j] == 'Q':
            QUEENS.append([i, j])
            break

    # down left
    for i, j in zip(range(x + 1, len(board)), range(y - 1, -1, -1)):
        if board[i][j] == 'Q':
            QUEENS.append([i, j])
            break

    # up left
    for i, j in zip(range(x - 1, -1, -1), range(y - 1, -1, -1)):
        if board[i][j] == 'Q':
            QUEENS.append([i, j])
            break


board = [input().split() for _ in range(8)]

queens_collision(board)


if QUEENS:
    [print(element) for element in QUEENS]
else:
    print("The king is safe!")

