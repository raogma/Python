def operate(num1, sign, num2):
    num1 = float(num1)
    num2 = float(num2)
    info = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2,
        '^': num1 ** num2,
    }
    return info[sign]
