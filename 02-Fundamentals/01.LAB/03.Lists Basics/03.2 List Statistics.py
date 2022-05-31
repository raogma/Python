numbers = int(input())

numbers = [int(input()) for _ in range(numbers)]
positives = [number for number in numbers if number >= 0]
negatives = [number for number in numbers if number < 0]

print(len(positives), sum(negatives))