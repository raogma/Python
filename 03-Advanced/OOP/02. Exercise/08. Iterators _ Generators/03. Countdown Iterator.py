class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.end = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.end < 0:
            raise StopIteration
        res, self.end = self.end, self.end - 1
        return res


for item in countdown_iterator(10):
    print(item, end=" ")