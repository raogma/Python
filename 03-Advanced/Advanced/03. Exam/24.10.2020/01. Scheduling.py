from sys import maxsize


def get_min(iterable):
    min_value = maxsize
    for num in iterable:
        if num <= min_value and num != 0:
            min_value = num
    return min_value


jobs = list(map(int, input().split(', ')))
target_idx = int(input())

cycles = 0

while True:
    current = get_min(jobs)
    cycles += current
    current_idx = jobs.index(current)
    if current_idx == target_idx:
        print(cycles)
        break
    jobs[current_idx] = 0
