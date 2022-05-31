def type_check(type):
    def inner(fn):
        def wrapper(*args):
            if not isinstance(*args, type):
                return "Bad Type"
            return fn(*args)
        return wrapper
    return inner


# type_check = lambda type: lambda fn: lambda *args: 'Bad Type' if not isinstance(*args, type) else fn(*args)


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))