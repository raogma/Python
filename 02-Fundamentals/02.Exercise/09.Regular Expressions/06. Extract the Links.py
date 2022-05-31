from re import finditer

line = input()
regex = r'www\.[a-zA-Z\d+]+((-)?[a-zA-Z\d+]+)*(\.[a-z]+)+'

while line:
    links = finditer(regex, line)

    for link in links:
        print(link.group())

    line = input()
