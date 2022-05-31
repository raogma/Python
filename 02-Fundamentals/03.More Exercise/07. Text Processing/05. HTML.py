def html_format(type, item):
    tags = {
        'title': ('<h1>', '</h1>'),
        'content': ('<article>', '</article>'),
        'comment': ('<div>', '</div>'),
    }
    return f'{tags[type][0]}\n    {item}\n{tags[type][1]}'


print(html_format('title', input()))
print(html_format('content', input()))
while True:
    command = input()
    if command == 'end of comments':
        break

    comment = command
    print(html_format('comment', comment))
