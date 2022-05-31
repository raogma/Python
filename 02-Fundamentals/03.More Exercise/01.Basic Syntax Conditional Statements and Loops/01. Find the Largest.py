number = input()

digits = [digit for digit in number]

print(''.join(sorted(digits, reverse=True)))