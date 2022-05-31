input_count = int(input())

odd, even = set(), set()

for i in range(1, input_count + 1):
    name = input()
    total = 0
    for ch in name:
        total += ord(ch)
    total //= i
    if total % 2 != 0:
        odd.add(total)
    else:
        even.add(total)

if sum(odd) == sum(even):
    print(', '.join(list(map(str, odd.union(even)))))
elif sum(odd) > sum(even):
    print(', '.join(list(map(str, odd.difference(even)))))
elif sum(even) > sum(odd):
    print(', '.join(list(map(str, even.symmetric_difference(odd)))))

