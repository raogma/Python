def add_to_set(set, len):
    for _ in range(len):
        set.add(input())


len_set_1, len_set_2 = list(map(int, input().split()))
set_1, set_2 = set(), set()

add_to_set(set_1, len_set_1)
add_to_set(set_2, len_set_2)

[print(element) for element in set_1.intersection(set_2)]
