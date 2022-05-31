mx = [input().split(', ') for _ in range(2)]
info = {mx[0][j]: mx[1][j] for j in range(len(mx[0]))}
[print(f'{country} -> {capital}') for country, capital in info.items()]
