txt = input()
nums, symbols = list(), list()
result, start = str(), int()

for i in range(len(txt)):
        nums.append(int(txt[i])) if txt[i].isnumeric() else symbols.append(txt[i])

take_list = [nums[i] for i in range(len(nums)) if i % 2 == 0]
skip_list = [nums[j] for j in range(len(nums)) if j % 2 != 0]

i, j = 0, 0
while i < len(take_list):
    while j < len(skip_list):
        result += ''.join(symbols[start: start + take_list[i]])
        start += take_list[i] + skip_list[j]
        i += 1
        j += 1

print(result)