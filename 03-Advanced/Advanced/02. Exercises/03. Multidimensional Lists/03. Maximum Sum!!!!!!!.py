from sys import maxsize
from copy import deepcopy


def make_square(starting_row_index, starting_col_index, size, list_to_fill, input_mx):
    index_to_fill = -1
    for r in range(starting_row_index, starting_row_index + size):
        index_to_fill += 1
        for c in range(starting_col_index, starting_col_index + size):
            list_to_fill[index_to_fill].append(input_mx[r][c])


def sum_sub_mx(list_to_sum):
    the_sum = 0
    for el in list_to_sum:
        the_sum += sum(el)
    return the_sum


def clear_sub_mx(list_to_clear):
    for el in list_to_clear:
        el.clear()


rows, cols = list(map(int, input().split()))
mx = [list(map(int, input().split())) for _ in range(rows)]
sub_mx_size = 3
max_sum = -maxsize
sub_mx = [[] for _ in range(sub_mx_size)]

for i in range(rows - (sub_mx_size - 1)):
    for j in range(cols - (sub_mx_size - 1)):
        make_square(i, j, sub_mx_size, sub_mx, mx)
        if sum_sub_mx(sub_mx) > max_sum:
            save_sub_mx = deepcopy(sub_mx)
            max_sum = sum_sub_mx(sub_mx)
        clear_sub_mx(sub_mx)

print(f'Sum = {max_sum}')
[print(' '.join(map(str, element))) for element in save_sub_mx]
