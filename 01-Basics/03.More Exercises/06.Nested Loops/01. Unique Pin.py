limit_first_num = int(input())
limit_second_num = int(input())
limit_third_num = int(input())

for first_num in range(1, limit_first_num + 1):
    if first_num % 2 == 0:
        for second_num in range(2, limit_second_num + 1):
                if second_num == 2 or second_num == 3 or second_num == 5 or second_num == 7:
                    for third_num in range(2, limit_third_num + 1):
                        if third_num % 2 == 0:
                            print(f"{first_num} {second_num} {third_num}")
