line = list(map(int, input().split(', ')))

data = {
    'Positive': [],
    'Negative': [],
    'Even': [],
    'Odd': [],
}
for num in line:
    if num >= 0:
        data['Positive'].append(num)
    else:
        data['Negative'].append(num)
    if num % 2 == 0:
        data['Even'].append(num)
    else:
        data['Odd'].append(num)

for element in data:
    print(f'{element}: {", ".join(list(map(str, data[element])))}')
