from math import ceil


def get_time(list, total_time=0):
    for element in list:
        if element == 0:
            total_time *= 0.8
        else:
            total_time += element
    return total_time


list_of_nums = input().split()
left = [int(list_of_nums[i]) for i in range(0, len(list_of_nums) // 2)]
right = [int(list_of_nums[j]) for j in range(len(list_of_nums) - 1, ceil(len(list_of_nums) / 2) - 1, -1)]

first_racer, second_racer = get_time(left), get_time(right)

if first_racer < second_racer:
    print(f'The winner is left with total time: {first_racer:.1f}')
elif first_racer == second_racer:
    print('Draw')
else:
    print(f'The winner is right with total time: {second_racer:.1f}')
