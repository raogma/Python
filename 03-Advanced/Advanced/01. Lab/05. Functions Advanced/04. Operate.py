def operate(operator, *args):
    def multiply(*nums):
        result = 1
        for num in nums:
            result *= num
        return result

    def divide(*nums):          # ACHTUNG!
        result = nums[0]
        for i in range(1, len(nums)):
            result /= nums[i]
        return result

    def subtract(*nums):        # ACHTUNG!
        result = nums[0]
        for i in range(1, len(nums)):
            result -= nums[i]
        return result

    if operator == '+':
        return sum(args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)


content1 = ["+", 1, 2, 3]
content2 = ["/", 3, 4]
print(operate(*content1))
print(operate(*content2))
