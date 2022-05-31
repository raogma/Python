class Stack:
    def __init__(self):
        self.store = []

    def push(self, element):
        return self.store.append(element)

    def peek(self):
        return self.store[-1]

    def pop(self):
        return self.store.pop(-1)

    def is_empty(self):
        return len(self.store) == 0


msg = Stack()

for ch in input():
    msg.push(ch)

while not msg.is_empty():
    print(msg.pop(), end='')

