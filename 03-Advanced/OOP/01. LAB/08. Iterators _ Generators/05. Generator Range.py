# I.
def genrange(start, end):
    if start < end:
        while start <= end:
            yield start
            start += 1
    else:
        while start >= end:
            yield start
            start -= 1


# II.
# genrange = lambda start, end: (i for i in range(start, end + 1))


print(list(genrange(10, 1)))

