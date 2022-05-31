degree = float(input())

if 26 <= degree <= 35:
    print("Hot")
elif 20.1 <= degree <= 25.9:
    print("Warm")
elif 15 <= degree <= 20:
    print("Mild")
elif 12 <= degree <= 14.9:
    print("Cool")
elif 5 <= degree <= 11.9:
    print("Cold")
else:
    print("unknown")