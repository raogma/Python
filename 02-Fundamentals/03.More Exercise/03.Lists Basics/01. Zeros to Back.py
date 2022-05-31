def change_type(list):
    for i in range(len(list)):
        list[i] = int(list[i])


def move_num(list, element):
    list.remove(element)
    list.append(element)


nums = input().split(', ')
change_type(nums)

for num in nums:
    if num == 0:
        move_num(nums, num)

print(nums)