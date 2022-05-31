def math_operations(*args, **kwargs):
    args = list(args)
    operations = ['a', 's', 'd', 'm']
    while args:
        op = operations.pop(0)
        num = args.pop(0)
        if op == 'a':
            kwargs[op] += num
        elif op == 's':
            kwargs[op] -= num
        elif op == 'd':
            if num != 0:
                kwargs[op] /= num
        elif op == 'm':
            kwargs[op] *= num
        operations.append(op)

    return kwargs


print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))