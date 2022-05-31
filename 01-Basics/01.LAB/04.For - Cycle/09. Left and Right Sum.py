first_sum = 0
second_sum = 0
num_of_numbers = int(input())

for num_of_numbers in range(1, num_of_numbers + 1):
    first_numbers = int(input())
    first_sum += first_numbers
for num_of_numbers in range(1, num_of_numbers + 1):
    second_numbers = int(input())
    second_sum += second_numbers

difference = abs(first_sum - second_sum)
if first_sum == second_sum:
    print(f"Yes, sum = {first_sum}")
else:
    print(f" No, diff = {difference}")