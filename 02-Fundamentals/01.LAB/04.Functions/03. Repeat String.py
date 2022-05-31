def repeat(text, times, new_text):
    for _ in range(times):
        for symbol in text:
            new_text += symbol
    return new_text


text = input()
times = int(input())
new_text = ' '
print(repeat(text, times, new_text))
