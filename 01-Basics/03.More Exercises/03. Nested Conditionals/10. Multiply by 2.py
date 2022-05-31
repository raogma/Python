from sys import maxsize
num_of_nums = maxsize
for num_of_nums in range(1, num_of_nums + 1):
    number = float(input())
    if number < 0:
        print("Negative number!")
        break
    else:
        print(f"Result: {number * 2:.2f}")
