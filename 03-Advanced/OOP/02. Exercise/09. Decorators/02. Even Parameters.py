ERROR: str = "Please use only even numbers!"


class even_parameters:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args):
        for num in args:
            if not isinstance(num, int) or num % 2 != 0:
                return ERROR
        res = self.fn(*args)
        return res

# def even_parameters(fn):
#     def wrapper(*args):
#         for num in args:
#             if not isinstance(num, int) or num % 2 != 0:
#                 return ERROR
#         res = fn(*args)
#         return res
#     return wrapper


# @even_parameters
# def add(a, b):
#     return a + b
#
#
# print(add(2, 4))
# print(add("Peter", 1))

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
