names_count = int(input())

unique_names = set()

for _ in range(names_count):
    unique_names.add(input())

[print(name) for name in unique_names]

