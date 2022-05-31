from functools import reduce
RESULT = []


def factorial(n):
    if n == 0:
        return
    global RESULT
    RESULT.append(n)
    factorial(n - 1)


factorial(5)

print(f"{' * '.join(map(str, RESULT))} = {reduce(lambda x,y: x*y, RESULT)}")