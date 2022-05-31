from re import finditer

regex = r'(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'
phones = finditer(regex, input())
phones = [phone.group(0) for phone in phones]

print(*phones, sep=', ')