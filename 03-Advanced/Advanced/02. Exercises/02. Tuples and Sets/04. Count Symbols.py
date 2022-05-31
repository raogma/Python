msg = input()

occurrences = dict()

for ch in msg:
    if ch not in occurrences:
        occurrences[ch] = 1
    else:
        occurrences[ch] += 1

[print(f'{ch}: {count} time/s') for ch, count in sorted(occurrences.items())]
