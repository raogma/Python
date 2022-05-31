PATH = r'/home/rei/Desktop/SoftUni/OOP/02. Exercise/09. Decorators/08. Store Results'


class store_results:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args):
        res = self.fn(*args)
        fn_name = self.fn.__name__
        global PATH
        with open(PATH + '/results.txt', 'a') as file:
            file.write(f"Function '{fn_name}' was called. Result: {res}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
