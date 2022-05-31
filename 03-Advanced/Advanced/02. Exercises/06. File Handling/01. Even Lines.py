def get_even_lines(file_path):
    with open(file_path) as read_file:
        lines = read_file.readlines()
    lines = [lines[i] for i in range(len(lines)) if i % 2 == 0]
    return lines


def make_reversed_lines(lines, ):
    for i in range(len(lines)):
        lines[i] = ' '.join(list(reversed(lines[i].split())))
    return lines


def replace_symbols(lines, ):
    symbols = ',?.!-'
    for i in range(len(lines)):
        for symbol in symbols:
            lines[i] = lines[i].replace(symbol, '@')
    return lines


input_path = r'/home/rei/Desktop/SoftUni/Advanced/02. Exercises/06. File Handling/Files/01. Еven Lines Files/text.txt'

needed_lines = get_even_lines(input_path)
needed_lines = make_reversed_lines(needed_lines)
needed_lines = replace_symbols(needed_lines)

[print(sentence) for sentence in needed_lines]

