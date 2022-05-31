class dictionary_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.__keys = list(self.iterable)
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self. __index == len(self.iterable):
            raise StopIteration
        key = self.__keys[self.__index]
        value = self.iterable[key]
        self.__index += 1
        return key, value


for x in dictionary_iter({1: "1", 2: "2"}):
    print(x)
