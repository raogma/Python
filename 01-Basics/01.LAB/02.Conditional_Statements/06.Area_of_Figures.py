from math import pi

shape = input()

if shape == "square":
    a = float(input())
    s = a ** 2
    print(f"{s:.3f}")

elif shape == "rectangle":
    a = float(input())
    b = float(input())
    s = a * b
    print(f"{s:.3f}")

elif shape == "circle":
    r = float(input())
    s = pi * r ** 2
    print(f"{s:.3f}")

elif shape == "triangle":
    a = float(input())
    h = float(input())
    s = a * h / 2
    print(f"{s:.3f}")