from random import randint


class RandomList(list):
    def get_random_element(self):
        index = randint(len(self) - 1)  # особеност на randint
        element = self[index]
        self.pop(index)
        return element


li = RandomList()
li.append(4)
li.append(3)
li.append(5)

print(li.get_random_element())