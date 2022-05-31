input_count = int(input())

periodic_table = set()

for _ in range(input_count):
    elements = input().split()
    while elements:
        element = elements.pop()
        periodic_table.add(element)

[print(element) for element in periodic_table]