numbers = int(input())
word = input()

non_filtered = []
filtered = []

for number in range(numbers):
    sentence = input()
    non_filtered.append(sentence)
    if word in sentence:
        filtered.append(sentence)

print(non_filtered)
print(filtered)