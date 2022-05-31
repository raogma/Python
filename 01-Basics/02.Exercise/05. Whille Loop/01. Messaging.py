nums = input().split()
string = input()
str_list = [ch for ch in string]
msg = str()

for num in nums:
    index = sum(int(num))
    if index >= len(string):
        index -= len(string)
    msg += str_list.pop(index)

print(msg)