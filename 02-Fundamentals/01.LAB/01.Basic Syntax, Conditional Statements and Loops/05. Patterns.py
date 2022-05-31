max_stars = int(input())

for rows in range(1, max_stars + 1):
    for columns in range(1, rows + 1):
        if rows != columns:
            print("*", end="")
        else:
            print("*")

for rows in range(max_stars - 1, 0, -1):
    for columns in range(1, rows + 1):
        if rows != columns:
            print("*", end="")
        else:
            print("*")