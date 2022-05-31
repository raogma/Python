from re import finditer
from re import split

data = input()
regex = r'([#\|])[a-zA-Z\s]+\1\d{2}/\d{2}/\d{2}\1([0-9]{1,4}|10000)\1'

total_calories = 0
res = str()

for element in finditer(regex, data):
    element = element.group()[1:-1]
    product, expiration, calories = split(r'\||#', element)
    total_calories += int(calories)
    res += f"Item: {product}, Best before: {expiration}, Nutrition: {calories}\n"

print(f"You have food to last you for: {total_calories//2000} days!\n" + res[:-1])