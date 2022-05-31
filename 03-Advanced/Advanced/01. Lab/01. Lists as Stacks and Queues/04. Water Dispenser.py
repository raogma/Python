from collections import deque
from sys import exit

quantity = float(input())
queue = deque()

while True:
    line = input()
    if line == 'Start':
        while True:
            line = input()
            if line == 'End':
                print(f'{int(quantity)} liters left')
                exit(0)
            elif line.isnumeric():
                if quantity - float(line) >= 0:
                    quantity -= float(line)
                    print(f'{queue.popleft()} got water')
                else:
                    print(f'{queue.popleft()} must wait')
            elif 'refill' in line:
                quantity += float(line.split()[1])
    else:
        queue.append(line)

