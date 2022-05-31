from sys import exit

a = int(input())
b = int(input())
max_passwords = int(input())

counter = 0

for A in range(35, 56):
    for B in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                counter += 1
                A += 1
                B += 1
                if x == a and y == b:
                    exit(0)
                if counter == max_passwords:
                    exit(0)
                if A > 55:
                    A = 35
                if B > 96:
                    B = 64