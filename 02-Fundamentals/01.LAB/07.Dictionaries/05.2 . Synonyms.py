num = int(input())

syn_dict = {}

for _ in range(num):
    word = input()
    synonym = input()
    if word not in syn_dict:
        syn_dict[word] = []
    syn_dict[word].append(synonym)

[print(f'{key} - {", ".join(value)}') for key, value in syn_dict.items()]