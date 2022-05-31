magic_num = int(input())

counter = 0
i = 0
j = 0
k = 0
l = 0

for a in range(1, 10):
    for b in range(1, 10):
        if b > a:
            for c in range(1, 10):
                for d in range(1, 10):
                    if c > d and a * b + c * d == magic_num:
                        print(f"{a}{b}{c}{d}", end=" ")
                        counter += 1
                        if counter == 4:
                            i = a
                            j = b
                            k = c
                            l = d
if counter < 4:
    print()
    print("No!")
else:
    print()
    print(f"Password: {i}{j}{k}{l}")
