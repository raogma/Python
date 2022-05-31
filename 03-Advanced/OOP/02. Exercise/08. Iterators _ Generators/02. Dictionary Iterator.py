class dictionary_iter:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        for key in self.iterable:
            while self.iterable:
                save_key = key
                value = self.iterable.pop(key)
                return save_key, value
        raise StopIteration


for x in dictionary_iter({1: "1", 2: "2"}):
    print(x)
