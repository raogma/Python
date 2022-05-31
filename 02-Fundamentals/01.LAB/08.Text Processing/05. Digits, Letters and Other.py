txt = input()

nums, letters, other = str(), str(), str()

for i in range(len(txt)):
    if txt[i].isnumeric():
        nums += txt[i]
    elif txt[i].isalpha():
        letters += txt[i]
    else:
        other += txt[i]

print(f'{nums}\n{letters}\n{other}')