key = int(input())
n_lines = int(input())

msg = [chr(ord(input()) + key) for _ in range(n_lines)]

print(*msg, sep='')