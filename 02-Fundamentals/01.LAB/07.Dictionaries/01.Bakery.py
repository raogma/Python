line = input().split()

bakery_dict = {line[index]: int(line[index + 1]) for index in range(0, len(line), 2)}

print(bakery_dict)
