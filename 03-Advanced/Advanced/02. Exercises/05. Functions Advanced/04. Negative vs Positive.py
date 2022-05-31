def polarity(lst):
    pos = sum(list(filter(lambda x: x >= 0, lst)))
    neg = sum(list(filter(lambda x: x < 0, lst)))
    result = f'''
{neg}
{pos}'''
    if pos > abs(neg):
        result += '\nThe positives are stronger than the negatives'
    elif pos < abs(neg):
        result += '\nThe negatives are stronger than the positives'
    else:
        result += '\nEqual'

    return result


print(polarity(list(map(int, input().split()))))