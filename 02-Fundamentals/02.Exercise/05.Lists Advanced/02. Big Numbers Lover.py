string_l = input().split()
sorted_l = sorted(string_l)[::-1]
biggest_num = ''

for element in sorted_l:
    biggest_num += element

print(biggest_num)