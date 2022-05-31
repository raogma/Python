from sys import exit

activities = 'coding, movie, dog, cat'
counter = 0
while True:
    command = input()
    if command == 'END':
        break

    if command.islower() and command in activities.lower():
        counter += 1
    elif command.isupper() and command in activities.upper():
        counter += 2
    if counter > 5:
        print(f'You need extra sleep')
        exit(0)

print(counter)
