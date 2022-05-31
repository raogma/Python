from re import finditer


def fill(iterable: dict, item: str):
    for key in iterable:
        if item[-1] == iterable[key]:
            if item[-1] == '$':
                iterable[key] = ''.join(item[:-1])
                break
            iterable[key] = ''.join(item[1:-1])
            break


regex = r'(?P<name>%[A-Z][a-z]+%)|(?P<product><\w+>)|(?P<count>\|\d+\|)|(?P<price>\d+(.\d+)?\$)'
income = 0

while True:
    data = {
        'name': '%',
        'product': '>',
        'count': '|',
        'price': '$',
    }
    line = input()
    if line == 'end of shift':
        print(f"Total income: {income:.2f}")
        break
    i = 0
    for element in finditer(regex, line):
        element = [x for x in element.group() if x is not None]
        fill(data, element)
        i += 1
    if i == 4:
        print(f'{data["name"]}: {data["product"]} - {int(data["count"]) * float(data["price"]):.2f}')
        income += int(data['count']) * float(data['price'])