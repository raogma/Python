input_count = int(input())

intersections = list()

for _ in range(input_count):
    line = input().split('-')
    first_start, first_end = list(map(int, line[0].split(',')))
    second_start, second_end = list(map(int, line[1].split(',')))
    a = {x for x in range(first_start, first_end + 1)}
    b = {x for x in range(second_start, second_end + 1)}
    intersections.append(list(a.intersection(b)))

print(f'Longest intersection is {max(intersections, key=len)} with length {len(max(intersections, key=len))}')
