from sys import exit

numbers_str = input().split(',')
beggars = int(input())

beggars_list = [0] * beggars
numbers_list = [int(number_str) for number_str in numbers_str]

for index_beggars in range(0, len(beggars_list)):
    for index_numbers in range(0, len(numbers_list)):
        beggars_list[index_beggars] += (numbers_list[index_numbers])
        index_beggars += 1
        if index_beggars == len(beggars_list):
            index_beggars = 0
        if index_numbers == len(numbers_list) - 1:
            print(beggars_list)
            exit(0)


