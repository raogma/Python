words_l = input().split('.')
nums_l = [int(word) for word in words_l]
next_version_str = ''

for i in range(len(nums_l) - 1, -1, -1):
    if nums_l[i] + 1 == 10:
        nums_l[i] = 0
        continue
    else:
        nums_l[i] += 1
        break

for j in range(len(nums_l)):
    next_version_str += str(nums_l[j])
    if j == len(nums_l) - 1:
        break
    next_version_str += '.'

print(next_version_str)
