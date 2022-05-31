from collections import deque

contestants = deque(input().split())
toss = int(input())

counter = 0
while contestants:
    counter += 1
    person = contestants.popleft()
    if counter == toss:
        counter = 0
        if len(contestants) > 0:
            print(f'Removed {person}')
        else:
            print(f'Last is {person}')
    else:
        contestants.append(person)


