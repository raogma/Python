class Stack:
    def __init__(self):
        self.store = []

    def push(self, element):
        return self.store.append(element)

    def pop(self):
        return self.store.pop()

    def peek(self):
        return self.store[-1]


s = Stack()
expr = input()

for i in range(len(expr)):
    if expr[i] == '(':
        s.push(i)
    elif expr[i] == ')':
        start = s.peek()
        s.pop()
        print(expr[start:i + 1])
