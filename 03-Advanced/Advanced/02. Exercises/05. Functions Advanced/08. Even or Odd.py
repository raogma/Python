def even_odd(*args):
    args = list(args)
    command = args.pop(-1)
    if command == 'odd':
        return list(filter(lambda x: x % 2 != 0, args))
    if command == 'even':
        return list(filter(lambda x: x % 2 == 0, args))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
