def multiply_three(list, negative_count=0):
    for element in list:
        if element == 0:
            return 'zero'
        if element < 0:
            negative_count += 1
    return 'positive' if negative_count % 2 == 0 else 'negative'


nums = [float(input()) for _ in range(3)]

print(multiply_three(nums))
