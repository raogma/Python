times = int(input())

capacity = 255
total = 0

for time in range(times):
    amount = int(input())
    total += amount
    if total > capacity:
        print("Insufficient capacity!")
        total -= amount
print(total)
