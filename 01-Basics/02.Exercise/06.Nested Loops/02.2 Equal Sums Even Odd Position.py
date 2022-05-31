start = int(input())
end = int(input())

odd_sum = 0
even_sum = 0

for number in range(start, end + 1):
    number_to_string = str(number)
    for position, digit in enumerate(number_to_string):
        if position % 2 == 0:   #odd
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(number, end=" ")
    odd_sum = 0
    even_sum = 0
