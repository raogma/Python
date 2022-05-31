words = input().split()

while True:
    command = input()
    if command == 'Stop':
        print(' '.join(words))
        break

    command = command.split()

    if command[0] == 'Delete':
        index = int(command[1])
        if 0 <= index + 1 < len(words):
            words.pop(index + 1)

    elif command[0] == 'Swap':
        word1, word2 = command[1], command[2]
        if word1 in words and word2 in words:
            i1 = words.index(word1)
            i2 = words.index(word2)
            words[i1] = word2
            words[i2] = word1

    elif command[0] == 'Put':
        word, index = command[1], int(command[2])
        if 0 <= index - 1 <= len(words):
            words.insert(index - 1, word)

    elif command[0] == 'Sort':
        words = list(sorted(words, reverse=True))

    elif command[0] == 'Replace':
        word1, word2 = command[1], command[2]
        if word2 in words:
            i = words.index(word2)
            words[i] = word1
