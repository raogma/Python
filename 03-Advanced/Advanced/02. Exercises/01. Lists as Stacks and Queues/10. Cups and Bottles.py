from collections import deque
cups = deque(map(lambda x: int(x), input().split()))
bottles = deque(map(lambda x: int(x), input().split()))

wasted_litters = 0

while bottles and cups:
    bottle = bottles.pop()
    cup = cups.popleft()
    if cup > bottle:
        cup -= bottle
        cups.appendleft(cup)
    else:
        wasted_litters += bottle - cup

if not cups:
    print(f"Bottles: {' '.join(list(map(lambda x: str(x), bottles))[::-1])}")

elif not bottles:
    print(f"Cups: {' '.join(list(map(lambda x: str(x), cups)))}")

print(f"Wasted litters of water: {wasted_litters}")