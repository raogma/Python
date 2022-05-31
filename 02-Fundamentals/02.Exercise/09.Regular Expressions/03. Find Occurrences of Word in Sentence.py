from re import IGNORECASE
from re import findall

line = input()
word = input()

regex = f'\\b{word}\\b'
matches = findall(regex, line, flags=IGNORECASE)

print(len(matches))