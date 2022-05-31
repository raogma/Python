from sys import maxsize

pairs = int(input())
previous_sum = int(input()) + int(input())
max_difference = -maxsize
difference = 0

for pair in range(pairs - 1):     # not +1 cos of line 4
    current_sum = int(input()) + int(input())
    difference = abs(previous_sum - current_sum)
    if difference > max_difference:
        max_difference = difference

    previous_sum = current_sum

if pairs == 1:
    print(f"Yes, value={previous_sum}")
elif max_difference == 0:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={max_difference}")