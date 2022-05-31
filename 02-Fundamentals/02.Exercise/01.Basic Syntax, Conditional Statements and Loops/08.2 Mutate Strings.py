str_one = input()
str_two = input()

for current_index in range(0, len(str_one)):
    if str_one[current_index] != str_two[current_index]:
        for swap_index in range(0, current_index + 1):
            print(str_two[swap_index], end="")
        for remaining_index in range(current_index + 1, len(str_one)):
            print(str_one[remaining_index], end="")
        print()
