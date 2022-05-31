class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    value = float(input())
    if value < 0:
        raise ValueCannotBeNegative