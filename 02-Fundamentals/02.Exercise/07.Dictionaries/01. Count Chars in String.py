def append_to_dict(key, value, dictionary):
    if key not in dictionary.keys():
         dictionary[key] = value
    else:
        dictionary[key] += value


line = input().split()

symbols_dict = {}

for element in line:
    for symbol in element:
        append_to_dict(symbol, 1, symbols_dict)

[print(f'{key} -> {value}') for key, value in symbols_dict.items()]