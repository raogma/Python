from re import MULTILINE
from re import finditer

regex = r'^>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)$'
furniture = ['Bought furniture:']
total_sum = 0

while True:
    line = input()
    if line == 'Purchase':
        break

    order = finditer(regex, line, flags=MULTILINE)

    for x in order:
        furniture.append(x.group('furniture'))
        total_sum += int(x.group('quantity')) * float(x.group('price'))

[print(element) for element in furniture]
print(f'Total money spend: {total_sum:.2f}')