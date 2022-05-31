words = input().replace('.', '')
nw_v = int(words) + 1
nw_v_str = str(nw_v)
new_version = ''

for i in range(len(nw_v_str)):
    new_version += nw_v_str[i]
    if i == len(nw_v_str) - 1:
        break
    new_version += '.'

print(new_version)