def get_round_values(*args):
    result = [round(num) for num in args]
    return result


nums = list(map(float, input().split()))
print(get_round_values(*nums))