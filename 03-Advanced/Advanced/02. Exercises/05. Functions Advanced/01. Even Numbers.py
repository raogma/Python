def get_even_nums(lst):
    return list(filter(lambda x: x % 2 == 0, lst))


print(get_even_nums(list(map(int, input().split()))))
