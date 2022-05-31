txt = input().lower()

key_words = ["sand", "water", "fish", "sun"]

counter = 0
for word in key_words:
    while word in txt:
        txt = txt.replace(word, str(), 1)
        counter += 1

print(counter)