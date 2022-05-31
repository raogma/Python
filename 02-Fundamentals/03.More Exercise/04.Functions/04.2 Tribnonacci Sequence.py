def trib_sequence(count, default, i=0):
    if len(default) > count:
        return
    if len(default) == count:
        return

    default.append(sum(default[i:]))
    trib_sequence(count, default, i + 1)


number = int(input())
sequence = [1, 1, 2]
trib_sequence(number, sequence)
print(' '.join(list(map(str, sequence[0:number]))))

