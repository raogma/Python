size = int(input())
sq_mx = [input().split(', ') for _ in range(size)]

primary_diag = [sq_mx[i][i] for i in range(size)]
secondary_diag = []

i = 0
while i != size:
    for j in range(size - 1, -1, -1):
        secondary_diag.append(sq_mx[i][j])
        i += 1

print(f'''
First diagonal: {", ".join(primary_diag)}. Sum: {sum(map(int, primary_diag))}
Second diagonal: {", ".join(secondary_diag)}. Sum: {sum(map(int, secondary_diag))}
''')
