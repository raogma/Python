def logged(fn):
    def wrapper(*args):
        res = fn(*args)
        return f'''you called {fn.__name__}{args}
it returned {res}'''
    return wrapper


# logged = lambda fn: lambda *args: f'you called {fn.__name__}{args}\nit returned {fn(*args)}'


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))