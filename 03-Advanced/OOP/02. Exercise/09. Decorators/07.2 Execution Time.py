from timeit import default_timer


def exec_time(fn):
    def wrapper(*args):
        start_time = default_timer()
        fn(*args)
        end_time = default_timer()
        res = end_time - start_time
        return res
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))