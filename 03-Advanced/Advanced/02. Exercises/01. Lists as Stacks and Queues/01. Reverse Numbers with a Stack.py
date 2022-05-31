class Stack:
    def __init__(self):
        self.storage = []

    def pop(self):
        return self.storage.pop()

    def push(self, element):
        return self.storage.append(element)

    def is_empty(self):
        return len(self.storage) == 0


s = Stack()

[s.push(element) for element in input().split()]

while not s.is_empty():
    print(s.pop(), end=' ')