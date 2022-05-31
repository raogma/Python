def odd_or_even(command, lst):
    if command == 'Odd':
        return sum(list(filter(lambda x: x % 2 != 0, lst))) * len(lst)
    elif command == 'Even':
        return sum(list(filter(lambda x: x % 2 == 0, lst))) * len(lst)


print(odd_or_even(input(), list(map(int, input().split()))))
