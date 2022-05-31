total_number = int(input())
current_number = 1
for rows in range(1, total_number + 1):
    for columns in range(1, rows + 1):
        if columns != rows:
            print(f"{current_number}", end=" ")
        else:
            print(current_number)
        current_number += 1
        if current_number > total_number:
            break
    if current_number > total_number:
        break