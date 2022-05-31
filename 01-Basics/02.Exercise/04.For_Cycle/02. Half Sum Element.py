from sys import maxsize

num_of_nums = int(input())

max = -maxsize
sum_of_nums = 0
for num_of_nums in range(1, num_of_nums + 1):
    number = int(input())
    sum_of_nums += number
    if number >= max:
        max = number

sum_of_small_nums = sum_of_nums - max
difference = abs(max - sum_of_small_nums)

if sum_of_small_nums == max:
    print("Yes")
    print(f"Sum = {max}")
else:
    print("No")
    print(f"Diff = {difference}")