def append_to_dict(key, value, dictionary):
    if key not in dictionary.keys():
         dictionary[key] = value
    else:
        dictionary[key] += value


mine = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    append_to_dict(resource, quantity, mine)

[print(f'{key} -> {value}') for key, value in mine.items()]

