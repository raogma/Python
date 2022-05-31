max_stars = int(input())

for rows in range(1, max_stars + 1):
    print("*" * rows)
for rows in range(max_stars - 1, 0, -1):
    print("*" * rows)