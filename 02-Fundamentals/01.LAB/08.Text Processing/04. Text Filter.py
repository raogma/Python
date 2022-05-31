banned_words = input().split(', ')
txt = input()

for word in banned_words:
    while word in txt:
        txt = txt.replace(word, '*' * len(word))

print(txt)