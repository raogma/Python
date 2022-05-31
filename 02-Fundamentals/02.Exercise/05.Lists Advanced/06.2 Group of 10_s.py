from math import ceil
nums_str = input().split(', ')
nums_l = [int(element) for element in nums_str]

max_num = max(nums_l)

for group in range(1, ceil(max_num / 10) + 1):
    group_list = [num for num in nums_l if (group - 1) * 10 < num <= group * 10]
    print(f"Group of {group}0's: {group_list}")