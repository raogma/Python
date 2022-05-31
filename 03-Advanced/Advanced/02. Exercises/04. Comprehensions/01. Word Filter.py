txt = input().split()
txt = [element for element in txt if len(element) % 2 == 0]
[print(element) for element in txt]
