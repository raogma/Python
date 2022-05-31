beginning = int(input())
end = int(input())
magic_num = int(input())
counter = 0
isFound = False
for first_num in range(beginning, end + 1):
    for second_num in range(beginning, end + 1):
        counter += 1
        if first_num + second_num == magic_num:
            print(f"Combination N:{counter} ({first_num} + {second_num} = {magic_num})")
            isFound = True
            break
    if isFound:
        break
else:
    print(f"{counter} combinations - neither equals {magic_num}")