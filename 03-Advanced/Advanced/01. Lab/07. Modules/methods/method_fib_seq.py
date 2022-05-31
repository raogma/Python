def fib_seq(count):
    sequence = [0, 1]
    for i in range(count - 2):
        sequence.append(sum(sequence[i:]))
    return sequence


def find_num(array, num):
    if num in array:
        return f"The number - {num} is at index {array.index(num)}"
    return f"The number {num} is not in the sequence"
