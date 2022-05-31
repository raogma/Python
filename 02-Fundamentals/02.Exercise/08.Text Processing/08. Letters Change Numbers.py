line = input().split()
alphabet = dict()

for i in range(65, 91):
 alphabet[chr(i)] = int(i - 64)

result = int()
for element in line:
 first_let, last_let = element[0], element[-1]
 num = int(element[1: len(element) - 1])

 if first_let.isupper():
  num /= alphabet[first_let]
 elif first_let.islower():
  first_let = first_let.upper()
  num *= alphabet[first_let]
 if last_let.isupper():
  num -= alphabet[last_let]
 elif last_let.islower():
  last_let = last_let.upper()
  num += alphabet[last_let]

 result += num

print(f'{round(result, 2):.2f}')
