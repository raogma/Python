def ascii(start, end):
    in_between = " "
    if ord(start) > ord(end):
        for number in range(ord(end) + 1, ord(start)):
            in_between += chr(number)
            in_between += " "
    else:
        for number in range(ord(start) + 1, ord(end)):
             in_between += chr(number)
             in_between += " "
    return in_between


first_char = input()
second_char = input()
print(ascii(first_char, second_char))