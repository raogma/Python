start_num = int(input())
end_num = int(input())
odd_sum = 0
even_sum = 0

for number in range(start_num, end_num + 1):
    number_to_str = str(number)
    for digits in range(0, 6, 2): #odd
        odd_sum += int(number_to_str[digits])
    for digits in range(1, 6, 2): #even
        even_sum += int(number_to_str[digits])
    if even_sum == odd_sum:
        print(number, end=" ")
    odd_sum = 0
    even_sum = 0
