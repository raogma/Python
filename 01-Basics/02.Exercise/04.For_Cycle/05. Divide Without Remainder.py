num_of_nums = int(input())
p1 = 0
p2 = 0
p3 = 0

for num_of_nums in range(1, num_of_nums + 1):
    number = int(input())
    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

p1_percent = p1 * 100 / num_of_nums
p2_percent = p2 * 100 / num_of_nums
p3_percent = p3 * 100 / num_of_nums

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")