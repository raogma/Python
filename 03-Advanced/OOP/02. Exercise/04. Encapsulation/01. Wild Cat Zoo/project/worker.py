class Worker:
    def __init__(self, name, age, salary):
        self.age = age
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"