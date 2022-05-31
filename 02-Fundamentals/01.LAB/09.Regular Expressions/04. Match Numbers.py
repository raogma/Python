from re import finditer

regex = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
nums = finditer(regex, input())
nums = [num.group() for num in nums]
print(*nums)