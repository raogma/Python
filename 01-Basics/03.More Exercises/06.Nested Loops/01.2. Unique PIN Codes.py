limit_1 = int(input())
limit_2 = int(input())
limit_3 = int(input())

isSecond_prime = True

for number_1 in range(2, limit_1 + 1):
    if number_1 % 2 == 0:
        for number_2 in range(2, limit_2 + 1):
            for divider in range(2, number_2):
                if number_2 % divider == 0:
                    isSecond_prime = False
                    break
            else:
                for number_3 in range(2, limit_3 + 1):
                    if number_3 % 2 == 0:
                        print(f"{number_1} {number_2} {number_3}")
