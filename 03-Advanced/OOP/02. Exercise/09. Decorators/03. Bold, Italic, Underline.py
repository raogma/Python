def make_bold(fn):
    def wrapper(*args):
        res = fn(*args)
        return f'<b>{res}</b>'
    return wrapper


def make_italic(fn):
    def wrapper(*args):
        res = fn(*args)
        return f'<i>{res}</i>'
    return wrapper


def make_underline(fn):
    def wrapper(*args):
        res = fn(*args)
        return f'<u>{res}</u>'
    return wrapper

# make_bold = lambda fn: lambda *args: f'<b>{fn(*args)}</b>'
# make_italic = lambda fn: lambda *args: f'<i>{fn(*args)}</i>'
# make_underline = lambda fn: lambda *args: f'<u>{fn(*args)}</u>'


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))