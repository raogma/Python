num = int(input())

syn_dict = {}

while num != 0:
    num -= 1
    word = input()
    synonym = input()
    if word not in syn_dict:
        syn_dict[word] = synonym
        continue
    syn_dict[word] += ', ' + synonym

[print(f'{key} - {value}') for key, value in syn_dict.items()]