x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if (x == x2 and y == y1) or (x == x2 and y == y2) or (x == x1 and y == y2) or (x == x1 and y == y1):
    print("Border")
elif (x1 < x < x2 and y == y1) or (x1 < x < x2 and y == y2) or (x == x1 and y1 < y < y2)\
        or (x == x2 and y1 < y < y2):
    print("Border")
else:
    print("Inside / Outside")

