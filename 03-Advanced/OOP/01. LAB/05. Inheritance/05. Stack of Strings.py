class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        if isinstance(item, str):
            self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

    def __str__(self):
        return f'[{", ".join(reversed(self.data))}]'
