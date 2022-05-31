num_one_lv = int(input())
num_two_lv = int(input())
num_five_lv = int(input())
total = int(input())

for one_lv in range(0, num_one_lv + 1):
    for two_lv in range(0, num_two_lv + 1):
        for five_lv in range(0, num_five_lv + 1):
            if five_lv * 5 + two_lv * 2 + one_lv == total:
                print(f"{one_lv} * 1 lv. + {two_lv} * 2 lv. + {five_lv} * 5 lv. = {total} lv.")