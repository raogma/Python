def get_abs(*args):
    result = [abs(num) for num in args]
    return result


nums = list(map(float, input().split()))
print(get_abs(*nums))
