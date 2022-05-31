def print_triangle(num, max_num):
    if num == max_num + 1:
        return
    for i in range(1, num + 1):
        print(i, end=' ')
    print()
    print_triangle(num + 1, max_num)
    for i in range(1, num):
        print(i, end=' ')
    print()