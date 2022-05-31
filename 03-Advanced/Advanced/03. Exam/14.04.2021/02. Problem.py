def deduct_points(turn, iterable, total, player1_name, player2_name):
    if turn % 2 == 1:
        iterable[player1_name] -= total
    else:
        iterable[player2_name] -= total


def check_data(iterable):
    for key in iterable:
        if iterable[key] <= 0:
            return key


def count_turns(turn):
    if turn % 2 == 1:
        return (turn + 1) // 2
    else:
        return turn // 2


player1_name, player2_name = input().split(', ')
mx = [list(input().split(' ')) for _ in range(7)]

data = {
    player1_name: 501,
    player2_name: 501,
}

turn = 1
while True:
    r, c = list(map(int, input().strip('()').split(', ')))
    if 0 <= r < len(mx[0]) and 0 <= c < len(mx[0]):
        if mx[r][c] == 'B':
            total = 502
        elif mx[r][c] == 'D' or mx[r][c] == 'T':
            total = int(mx[r][0]) + int(mx[r][-1]) + int(mx[0][c]) + int(mx[-1][c])
            if mx[r][c] == 'D':
                total *= 2
            else:
                total *= 3
        else:
            total = int(mx[r][c])

        deduct_points(turn, data, int(total), player1_name, player2_name)
        winner = check_data(data)
        if winner is not None:
            break
    turn += 1

turn = count_turns(turn)
print(f"{winner} won the game with {turn} throws!")