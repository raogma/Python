from copy import deepcopy

cards_str = input()
shuffles = int(input())

cards_list = cards_str.split(" ")
first_half = []
second_half = []
shuffled_list = []

for shuffle in range(shuffles):
    if shuffle > 0:
        cards_list = deepcopy(shuffled_list)
        shuffled_list.clear()
        first_half.clear()
        second_half.clear()
        card_index = 0

    for card_index in range(0, int(len(cards_list) / 2)):
        first_half.append(cards_list[card_index])

    for card_index in range(int(len(cards_list) / 2), len(cards_list)):
        second_half.append(cards_list[card_index])

    for first_cards_i in range(len(first_half)):
        for second_cards_i in range(len(second_half)):
            shuffled_list.append(first_half[first_cards_i])
            shuffled_list.append(second_half[second_cards_i])
            first_cards_i += 1
            if len(shuffled_list) == len(cards_list):
                break
        if len(shuffled_list) == len(cards_list):
            break

print(shuffled_list)