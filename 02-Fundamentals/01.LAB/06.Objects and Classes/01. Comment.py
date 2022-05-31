class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


c = Comment('user1', 'I like this book')

print(c.username)
print(c.content)
print(c.likes)
