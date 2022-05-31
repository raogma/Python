from math import log, e

number = int(input())
base = input()
if base == 'natural':
    print(f'{log(number, e):.2f}')
else:
    print(f'{log(number, float(base)):.2f}')
