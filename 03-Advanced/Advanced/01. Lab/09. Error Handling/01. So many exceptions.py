numbers_list = input().split(", ")
result = 1

for num in numbers_list:
    num = int(num)
    if num <= 5:
        result *= num
    elif 5 < num <= 10:
        result /= num

print(result)
