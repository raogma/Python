class sequence_repeat:
    def __init__(self, sequence: str, number):
        self.number = number
        self.sequence = sequence
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.number > 0:
            if self.__index == len(self.sequence):
                self.__index = 0
            ch = self.sequence[self.__index]
            self.__index += 1
            self.number -= 1
            return ch
        raise StopIteration


for item in sequence_repeat('abc', 5):
    print(item, end='')