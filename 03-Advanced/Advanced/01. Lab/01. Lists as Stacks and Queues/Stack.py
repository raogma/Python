class Stack:
    def __init__(self):
        self.storage = []

    def peek(self):
        return self.storage[-1]

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    def isEmpty(self):
        return len(self.storage) == 0


# test

s = Stack()

[s.push(x) for x in range(5)]

while not s.isEmpty():
    print(s.pop())