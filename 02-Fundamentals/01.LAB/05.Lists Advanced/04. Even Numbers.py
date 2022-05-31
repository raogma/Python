string = input().split(', ')
nums_l = [int(element) for element in string]
indices_l = [i for i in range(len(nums_l)) if nums_l[i] % 2 == 0]

print(indices_l)