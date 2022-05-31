screening = input()
rows = int(input())
columns = int(input())

people = rows * columns

if screening == "Premiere":
    print(f"{people * 12:.2f} leva")
elif screening == "Normal":
    print(f"{people * 7.5:.2f} leva")
elif screening == "Discount":
    print(f"{people * 5:.2f} leva")
