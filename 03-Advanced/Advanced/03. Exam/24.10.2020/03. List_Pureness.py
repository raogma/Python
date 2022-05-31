def best_list_pureness(nums: list, K: int):
    purest_sum = 0
    for k in range(K + 1):
        sum = 0
        for i in range(len(nums)):
            sum += nums[i] * i
        if sum > purest_sum:
            purest_sum = sum
            purest_rotation = k
        nums.insert(0, nums.pop(-1))
    return f'Best pureness {purest_sum} after {purest_rotation} rotations'


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)