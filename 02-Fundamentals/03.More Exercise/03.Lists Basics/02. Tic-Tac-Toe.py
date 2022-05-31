def get_result(dictionary):
    for key in dictionary:
        if dictionary[key] == '111':
            return 'First player won'
        elif dictionary[key] == '222':
            return 'Second player won'
    else:
        return 'Draw!'


tictactoe = [input().split() for _ in range(3)]

rules_to_win = {
    'diag1': tictactoe[0][0] + tictactoe[1][1] + tictactoe[2][2],
    'diag2': tictactoe[0][2] + tictactoe[1][1] + tictactoe[2][0],
    'row1': tictactoe[0][0] + tictactoe[0][1] + tictactoe[0][2],
    'row2': tictactoe[1][0] + tictactoe[1][1] + tictactoe[1][2],
    'row3': tictactoe[2][0] + tictactoe[2][1] + tictactoe[2][2],
    'column1': tictactoe[0][0] + tictactoe[1][0] + tictactoe[2][0],
    'column2': tictactoe[0][1] + tictactoe[1][1] + tictactoe[2][1],
    'column3': tictactoe[0][2] + tictactoe[1][2] + tictactoe[2][2]
}

print(get_result(rules_to_win))