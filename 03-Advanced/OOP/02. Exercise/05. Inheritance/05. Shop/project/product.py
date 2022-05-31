class Product:
    def __init__(self,
                 name: str,
                 quantity: int):
        self.quantity = quantity
        self.name = name

    def increase(self, quantity):
        self.quantity += quantity

    def decrease(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity