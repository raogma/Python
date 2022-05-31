max_num_chars = int(input())

sum = 0

for chars in range(max_num_chars):
    char = input()
    sum += ord(char)

print(f"The sum equals: {sum}")