def vowel_filter(function):
    def wrapper():
        iterable = function()
        return [x for x in iterable if x.lower() in 'aeuio']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())