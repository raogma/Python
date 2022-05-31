n = int(input())
L = int(input())
# [97 : 122]
for first_symbol in range(1, n + 1):
    for second_symbol in range(1, n + 1):
        for third_symbol in range(97, 97 + L):
            for forth_symbol in range(97, 97 + L):
                for fifth_symbol in range(1, n + 1):
                    if fifth_symbol > first_symbol and fifth_symbol > second_symbol:
                        print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(forth_symbol)}{fifth_symbol}", end=" ")