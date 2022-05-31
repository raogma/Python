from sys import maxsize

numbers_str = input().split(" ")
remove_nums = int(input())

numbers_list = []                    # [10 9 8 7 6 5]
min_num = maxsize

for number_str in numbers_str:
    numbers_list.append(int(number_str))

for _ in range(remove_nums):
    for nums_index in range(len(numbers_list)):
        if numbers_list[nums_index] < min_num:
            min_num = numbers_list[nums_index]
    numbers_list.remove(min_num)
    min_num = maxsize
print(numbers_list)