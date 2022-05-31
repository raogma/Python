line = input().split()
words_dict = {}

for element in line:
    lower = element.lower()
    if lower not in words_dict:
        words_dict[lower] = 1
        continue
    words_dict[lower] += 1

[print(item, end=' ') for item, key in words_dict.items() if key % 2 != 0]