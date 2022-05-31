moves = int(input())

result = 0
total_result = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_nums = 0

for moves in range(1, moves + 1):
    move = int(input())
    if 0 <= move <= 9:
        result = 0.2 * move
        from_0_to_9 += 1
    elif 10 <= move <= 19:
        result = 0.3 * move
        from_10_to_19 += 1
    elif 20 <= move <= 29:
        result = 0.4 * move
        from_20_to_29 += 1
    elif 30 <= move <= 39:
        result = 50
        from_30_to_39 += 1
    elif 40 <= move <= 50:
        result = 100
        from_40_to_50 += 1

    if move < 0 or move > 50:
        total_result = total_result / 2
        invalid_nums += 1
    else:
        total_result += result


perc_from_0_to_9 = from_0_to_9 * 100 / moves
perc_from_10_to_19 = from_10_to_19 * 100 / moves
perc_from_20_to_29 = from_20_to_29 * 100 / moves
perc_from_30_to_39 = from_30_to_39 * 100 / moves
perc_from_40_to_50 = from_40_to_50 * 100 / moves
perc_invalid_nums = invalid_nums * 100 / moves

print(f"{total_result:.2f}")
print(f"From 0 to 9: {perc_from_0_to_9:.2f}%")
print(f"From 10 to 19: {perc_from_10_to_19:.2f}%")
print(f"From 20 to 29: {perc_from_20_to_29:.2f}%")
print(f"From 30 to 39: {perc_from_30_to_39:.2f}%")
print(f"From 40 to 50: {perc_from_40_to_50:.2f}%")
print(f"Invalid numbers: {perc_invalid_nums:.2f}%")

