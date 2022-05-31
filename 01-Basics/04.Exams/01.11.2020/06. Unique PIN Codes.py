limit1 = int(input())
limit2 = int(input())
limit3 = int(input())

isPrime = True

for a in range(2, limit1 + 1):
    for b in range(2, limit2 + 1):
        for divider in range(2, b):
            if b % divider == 0:
                isPrime = False
                break
        else:
            for c in range(2, limit3 + 1):
                if a % 2 == 0 and c % 2 == 0 and isPrime:
                    print(a, b, c)
