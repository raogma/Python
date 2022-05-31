def list_manipulation(list_to_append, list_to_check, element, next_element):
    if element in list_to_check:
        list_to_append.append(element)
        if element != next_element and len(list_to_append) < 6:
            list_to_append.clear()


tickets = input().split(',')

winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()
    first_half, second_half = list(), list()
    if len(ticket) != 20:
        print('invalid ticket')
        continue

    for i in range(0, len(ticket) // 2):
        list_manipulation(first_half, winning_symbols, ticket[i], ticket[i + 1])

    for i in range(len(ticket) // 2, len(ticket)):
        list_manipulation(second_half, winning_symbols, ticket[i], ticket[i + 1])
        if i == len(ticket) - 2:
            break

    last_symbol = ticket[-1]
    if last_symbol in winning_symbols:
        second_half.append(last_symbol)

    if len(first_half) < 6 or len(second_half) < 6:
        print(f'ticket "{ticket}" - no match')
    elif (6 <= len(first_half) <= 10 and 6 <= len(second_half) <= 9) or (6 <= len(first_half) <= 9 and 6 <= len(second_half) <= 10):
        print(f'ticket "{ticket}" - {min(len(first_half), len(second_half))}{first_half[0]}')
    elif len(first_half) == 10 and len(second_half) == 10:
        print(f'ticket "{ticket}" - {len(first_half)}{first_half[0]} Jackpot!')