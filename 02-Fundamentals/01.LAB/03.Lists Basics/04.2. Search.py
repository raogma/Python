numbers = int(input())
word = input()

sentences = [input() for _ in range(numbers)]

print(sentences)
print([sentence for sentence in sentences if word in sentence])