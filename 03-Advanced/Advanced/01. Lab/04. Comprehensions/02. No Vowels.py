txt = input()
print(''.join([ch for ch in txt if ch.lower() not in {'a', 'o', 'u', 'e', 'i'}]))
