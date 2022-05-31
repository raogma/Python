class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: object):
        self.products.append(product)

    def find(self, product_name: str):
        for element in self.products:
            if element.name == product_name:
                return element

    def remove(self, product_name: str):
        for element in self.products:
            if element.name == product_name:
                self.products.remove(element)

    def __repr__(self):
        res = ''
        for element in self.products:
            res += f"{element.name}: {element.quantity}\n"
        return res[:-1]

