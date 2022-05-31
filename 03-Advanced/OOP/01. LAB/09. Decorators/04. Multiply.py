def multiply(times):
    def inner(fn):
        def wrapper(number):
            result = fn(number)
            return result * times
        return wrapper
    return inner


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))