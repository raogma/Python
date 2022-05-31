def cache(fn):

    def wrapper(n):
        res = fn(n)
        wrapper.log[n] = res
        return res
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)