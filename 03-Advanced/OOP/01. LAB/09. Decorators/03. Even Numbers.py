def even_numbers(function):
    def wrapper(numbers):
        nums = function(numbers)
        return [x for x in nums if x % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))