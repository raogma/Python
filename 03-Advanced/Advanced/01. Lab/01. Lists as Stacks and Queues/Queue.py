class Queue:
    def __init__(self):
        self.storage = []
        self.start_index = 0

    def enqueue(self, element):
        return self.storage.append(element)

    def dequeue(self):
        first = self.storage[self.start_index]
        self.start_index += 1
        return first

    def peek(self):
        return self.storage[self.start_index]

    def isEmpty(self):
        return self.start_index == len(self.storage)


# test

q = Queue()

[q.enqueue(x) for x in range(5)]

while not q.isEmpty():
    print(q.dequeue())