from methods.method_operations import operate

data = input().split()
print(f'{operate(*data):.2f}')
