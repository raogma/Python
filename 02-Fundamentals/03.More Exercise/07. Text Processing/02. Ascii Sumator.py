def solution(x, y, iterable, sum=0):
    start = min(x, y)
    end = max(x, y)

    for num in iterable:
        if start < num < end:
            sum += num
    return sum


symbol1, symbol2 = map(ord, (input(), input()))
msg = list(map(ord, list(input())))

print(solution(symbol1, symbol2, msg))