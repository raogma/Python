class custom_range:
    def __init__(self, start, end):
        self.end = end
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        previous_start = self.start
        self.start += 1
        return previous_start


for num in custom_range(1, 10):
    print(num)