first_couple_start = int(input())
second_couple_start = int(input())
first_difference = int(input())
second_difference = int(input())

first_couple_end = first_difference + first_couple_start
second_couple_end = second_difference + second_couple_start

is_1stCouplePrime = True
is_2ndCouplePrime = True

for first_couple in range(first_couple_start, first_couple_end + 1):
    for divider1 in range(2, first_couple):
        if first_couple % divider1 == 0:
            is_1stCouplePrime = False
            break
        else:
            is_1stCouplePrime = True
    if not is_1stCouplePrime:
        continue
    for second_couple in range(second_couple_start, second_couple_end + 1):
        for divider2 in range(2, second_couple):
            if second_couple % divider2 == 0:
                is_2ndCouplePrime = False
                break
            else:
                is_2ndCouplePrime = True
        if not is_2ndCouplePrime:
            continue
        else:
            print(f"{first_couple}{second_couple}")
