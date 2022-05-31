from collections import deque
bullet_price = int(input())
barrel_size = int(input())
bullets = deque(map(lambda x: int(x), input().split()))
locks = deque(map(lambda x: int(x), input().split()))
intelligence = int(input())

shots_fired = 0

while bullets:
    if not locks:
        break
    bullet = bullets.pop()
    shots_fired += 1
    lock = locks.popleft()
    if bullet <= lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(lock)
    if len(bullets) > 0 and shots_fired % barrel_size == 0:
        print('Reloading!')

if len(bullets) == 0 and len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")

elif not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - (shots_fired * bullet_price)}")
