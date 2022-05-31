first_couple_start = int(input())
second_couple_start = int(input())
first_difference = int(input())
second_difference = int(input())

first_couple_end = first_difference + first_couple_start
second_couple_end = second_difference + second_couple_start

str_1st_couple_start = str(first_couple_start)
str_1st_couple_end = str(first_couple_end)
str_2nd_couple_start = str(second_couple_start)
str_2nd_couple_end = str(second_couple_end)

for first_digit in range(int(str_1st_couple_start[0]), int(str_1st_couple_end[0]) + 1):
    for second_digit in range(int(str_1st_couple_start[1]), int(str_1st_couple_end[1]) + 1):
        for third_digit in range(int(str_2nd_couple_start[0]), int(str_2nd_couple_end[0]) + 1):
            for forth_digit in range(int(str_2nd_couple_start[1]), int(str_2nd_couple_end[1]) + 1):
                print(f"{first_digit}{second_digit}{third_digit}{forth_digit}")
