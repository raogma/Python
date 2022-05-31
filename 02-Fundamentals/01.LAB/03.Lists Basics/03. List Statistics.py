numbers = int(input())

positive = []
negative = []

for number in range(numbers):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}. Sum of negatives: {sum(negative)}")