num_of_numbers = int(input())

odd_sum = 0
even_sum = 0

for num_of_numbers in range(1, num_of_numbers + 1):
    number = int(input())
    if num_of_numbers % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

difference = abs(odd_sum - even_sum)

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    print("No")
    print(f"Diff = {difference}")

