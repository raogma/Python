def tribonacci_sequence(input_num, sequence=[1], start_index=0, count=0):
    while input_num > 0:
        count += 1
        sequence.append(sum(sequence[start_index:len(sequence)]))
        if count > 2:
            start_index += 1
        input_num -= 1
    return sequence


num = int(input()) - 1

print(*tribonacci_sequence(num), sep=' ')
