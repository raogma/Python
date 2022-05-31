class Category:
    def __init__(self, id, name):
        self.id: int = id
        self.name: str = name

    def edit(self, new_name: str):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"