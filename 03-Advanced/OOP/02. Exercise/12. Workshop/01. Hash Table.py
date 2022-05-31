from typing import Any


class HashTable:
    def __init__(self):
        self.__capacity = 4
        self.__keys = [None] * self.__capacity
        self.__values = []

    def __getitem__(self, item):
        for key in self.__keys:
            if key == item:
                idx = self.__keys.index(key)
                return self.__values[idx]

    def __setitem__(self, key, value):
        for i in range(len(self.__keys)):
            if self.__keys[i] is None:
                self.__keys[i] = key
                break
        else:
            self.__keys += [None] * self.__capacity
            self.__keys[i + 1] = key

        self.__values.append(value)

    def __len__(self):
        return len(self.__keys)

    def get(self, item: str):
        for key in self.__keys:
            if key == item:
                idx = self.__keys.index(key)
                return self.__values[idx]


table = HashTable()

table["name"] = "Peter"
table["gender"] = "male"
table["hair"] = "brown"
table["height"] = 185
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
