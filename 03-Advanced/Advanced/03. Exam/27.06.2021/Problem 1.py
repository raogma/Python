from collections import deque

chocolates = list(map(int, input().split(', ')))
cups = deque(map(int, input().split(', ')))

milkshakes = 0

while milkshakes < 5 and len(cups) > 0 and len(chocolates) > 0:
    cup = cups.popleft()
    choc = chocolates.pop()
    if cup <= 0:
        if choc > 0:
            chocolates.append(choc)
            continue
    if choc <= 0:
        if cup > 0:
            cups.appendleft(cup)
            continue
    if choc == cup:
        milkshakes += 1
    else:
        cups.append(cup)
        choc -= 5
        chocolates.append(choc)


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join((list(map(str, chocolates))))}")
else:
    print("Chocolate: empty")

if cups:
    print(f"Milk: {', '.join((list(map(str, cups))))}")
else:
    print("Milk: empty")
