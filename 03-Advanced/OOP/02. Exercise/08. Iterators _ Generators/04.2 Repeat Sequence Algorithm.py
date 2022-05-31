class sequence_repeat:
    def __init__(self, sequence: str, number):
        self.number = number
        self.sequence = sequence
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.__index < self.number:
            saved_index = self.__index % len(self.sequence)
            self.__index += 1
            return self.sequence[saved_index]
        raise StopIteration


for item in sequence_repeat('abc', 5):
    print(item, end='')
############
# Algorithm#
# 0 % 3 = 0#
# 1 % 3 = 1#
# 2 % 3 = 2#
# 3 % 3 = 0#
# 4 % 3 = 1#
# 5 % 3 = 2#
# 6 % 3 = 0#
############