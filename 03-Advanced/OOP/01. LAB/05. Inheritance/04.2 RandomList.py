from random import choice


class RandomList(list):
    def get_random_element(self):
        element = choice(self)
        return self.pop(self.index(element))