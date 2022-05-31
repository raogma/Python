from sys import maxsize
total_electrons = int(input())

shells = maxsize
atom = []

while total_electrons != 0:
    for shell in range(1, shells + 1):
        electrons = 2 * shell ** 2
        if electrons > total_electrons:
            atom.append(total_electrons)
            total_electrons = 0
            break
        atom.append(electrons)
        total_electrons -= electrons

print(atom)
