from sys import exit

men = int(input())
women = int(input())
max_tables = int(input())

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        max_tables -= 1
        if max_tables >= 0:
            print(f"({man} <-> {woman})", end=" ")
        else:
            exit(0)