from collections import deque

queue = deque()

while True:
    line = input()
    if line == 'End':
        break
    elif line == 'Paid':
        while queue:
            print(queue.popleft())
    else:
        queue.append(line)

print(f'{len(queue)} people remaining.')