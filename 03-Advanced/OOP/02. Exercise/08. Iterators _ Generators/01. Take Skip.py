class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.num = 0
        self.needed_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.needed_count == self.count:
            raise StopIteration
        previous_num, self.num = self.num, self.num + self.step
        self.needed_count += 1
        return previous_num


for number in take_skip(2, 6):
    print(number)