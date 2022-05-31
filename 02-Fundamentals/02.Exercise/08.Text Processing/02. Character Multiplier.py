line = input().split()
ordered_line = sorted(line, key=lambda x: len(x))
str1, str2 = ordered_line[0], ordered_line[1]

total_sum = int()
for i in range(len(str1)):
    total_sum += ord(str1[i]) * ord(str2[i])

for j in range(len(str2) - 1, len(str1) - 1, -1):
    total_sum += ord(str2[j])

print(total_sum)
