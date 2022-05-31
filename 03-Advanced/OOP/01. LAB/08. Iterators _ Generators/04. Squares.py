# I.
# def squares(n):
#     for i in range(1, n + 1):
#         yield i ** 2

# II.
# squares = lambda n: (i ** 2 for i in range(1, n + 1))

# III.
def squares(n):
    i = 1
    while i <= n:
        yield i ** 2
        i += 1


print(list(squares(5)))