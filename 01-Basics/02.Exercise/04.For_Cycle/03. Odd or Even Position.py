from sys import maxsize

num_of_nums = int(input())
odd_max = - maxsize
odd_min = maxsize
odd_sum = 0
even_max = - maxsize
even_min = maxsize
even_sum = 0

for num_of_nums in range(1, num_of_nums + 1):
    number = float(input())
    if num_of_nums % 2 != 0:
        odd_sum += number
        if number >= odd_max:
            odd_max = number
        if number <= odd_min:
            odd_min = number
    elif num_of_nums % 2 == 0:
        even_sum += number
        if number >= even_max:
            even_max = number
        if number <= even_min:
            even_min = number

print(f"OddSum={odd_sum:.2f},")
if odd_min == maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")



