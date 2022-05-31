from sys import maxsize


def exchange(num_list, count):
    new_list = []
    for i in range(count + 1, len(num_list)):
        new_list.append(num_list[i])
    for i in range(0, count + 1):
        new_list.append(num_list[i])
    return new_list


def max_odd(num_list):
    max_num = -maxsize
    big_odd_index = None
    for j in range(len(num_list)):
        if num_list[j] % 2 != 0:
            if num_list[j] >= max_num:
                max_num = num_list[j]
                big_odd_index = j
    return big_odd_index


def max_even(num_list):
    max_num = -maxsize
    big_even_index = None
    for j in range(len(num_list)):
        if num_list[j] % 2 == 0:
            if num_list[j] >= max_num:
                max_num = num_list[j]
                big_even_index = j
    return big_even_index


def min_odd(num_list):
    min_num = maxsize
    small_odd_index = None
    for j in range(len(num_list)):
        if num_list[j] % 2 != 0:
            if num_list[j] <= min_num:
                min_num = num_list[j]
                small_odd_index = j
    return small_odd_index


def min_even(num_list):
    min_num = maxsize
    small_odd_index = None
    for j in range(len(num_list)):
        if num_list[j] % 2 == 0:
            if num_list[j] <= min_num:
                min_num = num_list[j]
                small_odd_index = j
    return small_odd_index


def first_odd(num_list, count):
    new_list = []
    for i in range(len(num_list)):
        if num_list[i] % 2 != 0:
            count -= 1
            new_list.append(num_list[i])
            if count == 0:
                return new_list
    return new_list


def first_even(num_list, count):
    new_list = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            count -= 1
            new_list.append(num_list[i])
            if count == 0:
                return new_list
    return new_list


def last_odd(num_list, count):
    new_list = []
    for i in range(len(num_list) - 1, -1, -1):
        if num_list[i] % 2 != 0:
            new_list.append(num_list[i])
            count -= 1
            if count == 0:
                return new_list[::-1]
    return new_list[::-1]


def last_even(num_list, count):
    new_list = []
    for i in range(len(num_list) - 1, -1, -1):
        if num_list[i] % 2 == 0:
            new_list.append(num_list[i])
            count -= 1
            if count == 0:
                return new_list[::-1]
    return new_list[::-1]



numbers_str = input().split(" ")
numbers_list = []

for element in numbers_str:
    numbers_list.append(int(element))

command = input()

while command != "end":
    command_list = command.split(" ")
    if command_list[0] == "exchange":
        index = int(command_list[1])     # index == count
        if index < 0 or index >= len(numbers_list):
            print("Invalid index")
        else:
            numbers_list = exchange(numbers_list, index)

    elif command_list[0] == "max":
        if command_list[1] == "odd":
            if max_odd(numbers_list) is None:
                print("No matches")
            else:
                print(max_odd(numbers_list))
        elif command_list[1] == "even":
            if max_even(numbers_list) is None:
                print("No matches")
            else:
                print(max_even(numbers_list))

    elif command_list[0] == "min":
        if command_list[1] == "odd":
            if min_odd(numbers_list) is None:
                print("No matches")
            else:
                print(min_odd(numbers_list))
        elif command_list[1] == "even":
            if min_even(numbers_list) is None:
                print("No matches")
            else:
                print(min_even(numbers_list))

    elif command_list[0] == "first":
        number = int(command_list[1])     # number == count
        if number == 0 or number > len(numbers_list):
            print("Invalid count")
        else:
            if command_list[2] == "odd":
                print(first_odd(numbers_list, number))
            elif command_list[2] == "even":
                print(first_even(numbers_list, number))

    elif command_list[0] == "last":
        number = int(command_list[1])     # number == count
        if number == 0 or number > len(numbers_list):
            print("Invalid count")
        else:
            if command_list[2] == "odd":
                print(last_odd(numbers_list, number))
            elif command_list[2] == "even":
                print(last_even(numbers_list, number))
    command = input()

print(numbers_list)