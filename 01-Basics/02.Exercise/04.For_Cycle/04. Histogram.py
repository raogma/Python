num_of_nums = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for num_of_nums in range(1, num_of_nums + 1):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

# x/100 * num_of_nums = p1
#x = p1 * 100 / num_of_nums

p1_percent = p1 * 100 / num_of_nums
p2_percent = p2 * 100 / num_of_nums
p3_percent = p3 * 100 / num_of_nums
p4_percent = p4 * 100 / num_of_nums
p5_percent = p5 * 100 / num_of_nums

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")