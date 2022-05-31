from collections import deque

soldiers = deque(input().split())
kill_step = int(input())
counter = 0
result = list()

while soldiers:
    counter += 1
    soldier = soldiers.popleft()
    if kill_step == counter:
        counter = 0
        result.append(soldier)
    else:
        soldiers.append(soldier)

print(f"[{','.join(result)}]")
