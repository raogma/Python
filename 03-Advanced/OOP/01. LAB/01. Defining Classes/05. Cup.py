class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, mls):
        if self.quantity + mls <= self.size:
            self.quantity += mls

    def status(self):
        if self.size < self.quantity:
            self.size = 0
        else:
            self.size -= self.quantity
        return self.size


cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())