execute = lambda fn, *args: fn(*args)


# def execute(fn, *args):
#     return fn(*args)


def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")


execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
