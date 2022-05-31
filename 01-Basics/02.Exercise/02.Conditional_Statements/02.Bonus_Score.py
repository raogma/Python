num = int(input())

if num <= 100:
    num_v2 = num + 5

elif num > 1000:
    num_v2 = num + 0.1 * num

else:
    num_v2 = num + 0.2 * num

if num % 2 == 0:
    num_v3 = num_v2 + 1
    print(num_v3 - num)
    print(num_v3)

elif num % 10 == 5:
    num_v3 = num_v2 + 2
    print(num_v3 - num)
    print(num_v3)

else:
    print(num_v2 - num)
    print(num_v2)
