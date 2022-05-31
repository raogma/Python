def concatenate(*args):
    result = str()
    for element in args:
        result += element
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))