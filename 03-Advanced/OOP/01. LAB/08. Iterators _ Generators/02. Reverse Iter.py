class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.end_index = len(self.iterable) - 1
        self.start_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.end_index < self.start_index:
            raise StopIteration
        previous_end_index = self.end_index
        self.end_index -= 1
        return self.iterable[previous_end_index]


for item in reverse_iter([1, 2, 3, 4]):
    print(item)