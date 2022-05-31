text = input()

index = int()
res = str()
start = int()

while index < len(text):
    if text[index].isdigit():
        num = text[index]
        next_index = 1

        if index + 1 < len(text) and text[index + 1].isdigit():
            num += text[index + 1]
            next_index = 2

        num = int(num)
        res += text[start: index] * num

        if index + 1 >= len(text):
            break

        start = index + next_index

    index += 1

res = res.upper()
print(f'Unique symbols used: {len(set(res))}')
print(res)
