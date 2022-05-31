numbers = int(input())

even = []
odd = []
negative = []
positive = []

for _ in range(numbers):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

word = input()
if word == "even":
    print(even)
elif word == "odd":
    print(odd)
elif word == "positive":
    print(positive)
elif word == "negative":
    print(negative)