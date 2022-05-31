word = input()

indices = [i for i in range(len(word)) if word[i].isupper()]

print(indices)