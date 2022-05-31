def change_type_to_int(list):
    for index in range(len(list)):
        list[index] = int(list[index])


n_rows = int(input())
sea = [input().split() for _ in range(n_rows)]
attack_coordinates = input().split()

for line in sea:
    change_type_to_int(line)

ships_destroyed = 0

for element in attack_coordinates:
    element = element.split('-')
    change_type_to_int(element)
    row, col = element[0], element[1]
    if sea[row][col] > 0:
        sea[row][col] -= 1
        if sea[row][col] == 0:
            ships_destroyed += 1

print(ships_destroyed)
# sea = [
# [1 0 0 1]
# [2 0 0 0]
# [0 3 0 1]
# ]


