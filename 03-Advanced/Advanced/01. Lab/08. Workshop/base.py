from board import create_board, enumerate_board, get_state_of_board
from validate_input import get_player_info, validate_position
from rules import rules
from sys import exit


def print_welcome_msg(iterable):
    result = str()
    result += f'This is the numeration of the board:\n'
    result += f'{get_state_of_board(enumerate_board(create_board()))}\n'
    for key in iterable:
        result += f'{key} starts first!'
        return result


def search_position(mx, num):
    for r in range(len(mx)):
        for c in range(len(mx[r])):
            if mx[r][c] == int(num):
                return r, c


info = get_player_info()
print(print_welcome_msg(info))
nummed_board = enumerate_board(create_board())
board = create_board()

busy_positions = []
while True:
    for player in info:
        position = validate_position(busy_positions, player)
        busy_positions.append(position)
        i, j = search_position(nummed_board, position)
        board[i][j] = info[player]
        print(get_state_of_board(board))
        symbol = rules(board, busy_positions)
        if symbol == 'Draw!':
            print(symbol)
            exit(0)
        else:
            for player in info:
                if info[player] == symbol:
                    print(f'{player} won!')
                    exit(0)
