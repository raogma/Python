start = int(input())
end = int(input())

for first_num in range(start, end + 1):
    for second_num in range(start, end + 1):
        for third_num in range(start, end + 1):
            for forth_num in range(start, end + 1):
                if ((first_num % 2 == 0 and forth_num % 2 != 0)\
                        or (first_num % 2 != 0 and forth_num % 2 == 0))\
                        and first_num > forth_num\
                        and (second_num + third_num) % 2 == 0:
                    print(f"{first_num}{second_num}{third_num}{forth_num}", end=" ")