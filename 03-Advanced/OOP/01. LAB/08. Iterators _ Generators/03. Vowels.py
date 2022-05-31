special_chars = 'aeiuyo'


class vowels:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if self.isVowel(char):
                return char
        raise StopIteration

    @staticmethod
    def isVowel(char):
        global special_chars
        if char.lower() in special_chars:
            return char


for char in vowels('Abcedifuty0o'):
    print(char)
