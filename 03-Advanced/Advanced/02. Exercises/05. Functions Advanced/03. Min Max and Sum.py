def get_values(lst):
    return f'''
The minimum number is {min(lst)}
The maximum number is {max(lst)}
The sum number is: {sum(lst)}'''


print(get_values(list(map(int, input().split()))))
