line = input().split(', ')

for i in range(1, len(line) + 1):
    if line[-i] == 'wolf':
        if i == 1:
            print("Please go away and stop eating my sheep")
            break
        else:
            print(f'Oi! Sheep number {i - 1}! You are about to be eaten by a wolf!')
            break

