class Stack:
    def __init__(self):
        self.storage = []

    def push(self, element):
        return self.storage.append(element)

    def pop(self):
        return self.storage.pop()

    def max(self):
        return max(self.storage)

    def min(self):
        return min(self.storage)

    def is_empty(self):
        return len(self.storage) == 0

    def show(self):
        return self.storage


def solve(stack, command, to_print=False):
    if command[0] == '1':
        command = command.split()
        return to_print, stack.push(int(command[1]))
    elif command[0] == '2':
        return to_print, stack.pop()
    elif command[0] == '3':
        to_print = True
        return to_print, stack.max()
    elif command[0] == '4':
        to_print = True
        return to_print, stack.min()


s = Stack()

n_lines = int(input())
for _ in range(n_lines):
    line = input()
    if solve(s, line)[0]:
        print(solve(s, line)[1])
    else:
        solve(s, line)

print(s.show())
