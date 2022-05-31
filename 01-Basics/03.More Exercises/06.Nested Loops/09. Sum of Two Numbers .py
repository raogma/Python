from sys import exit
start = int(input())
end = int(input())
magic_num = int(input())

counter = 0

for first_num in range(start, end + 1):
    for second_num in range(start, end + 1):
        counter += 1
        if first_num + second_num == magic_num:
            print(f"Combination N:{counter} ({first_num} + {second_num} = {magic_num})")
            exit(0)
else:
    print(f"{counter} combinations - neither equals {magic_num}")