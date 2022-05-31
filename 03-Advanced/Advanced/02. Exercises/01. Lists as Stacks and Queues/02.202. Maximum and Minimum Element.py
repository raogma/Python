n_lines = int(input())
nums = list()

for _ in range(n_lines):
    line = input()
    if line.startswith('1'):
       line = line.split()
       nums.append(int(line[1]))
       continue
    if nums:
        if line.startswith('2'):
            nums.pop()
        elif line.startswith('3'):
            print(max(nums))
        elif line.startswith('4'):
            print(min(nums))
        else:
            print('Invalid command')

print(', '.join(map(lambda x: str(x), nums[::-1])))