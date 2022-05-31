def decrypting_msg(list_nums, list_str, msg=str()):
    for num in list_nums:
        sum_num = 0
        for digit in num:
            sum_num += int(digit)
        index = sum_num
        if index >= len(string):
            index -= len(string)
        msg += list_str.pop(index)
    return msg


nums = input().split()
string = input()
str_list = [ch for ch in string]

print(decrypting_msg(nums, str_list))