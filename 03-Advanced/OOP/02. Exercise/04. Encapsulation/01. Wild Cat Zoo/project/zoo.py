class Zoo:
    def __init__(self,
                 name: str,
                 budget: int,
                 animal_capacity: int,
                 workers_capacity: int,
                 ):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: object, price):
        if price <= self.__budget:
            if len(self.animals) < self.__animal_capacity:
                if animal not in self.animals:
                    self.__budget -= price
                    self.animals.append(animal)               # !NB
                    return f"{animal.name} the {type(animal).__name__} added to the zoo"
                return 'Animal is already in the zoo'
            return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker: object):
        if len(self.workers) < self.__workers_capacity:
            if worker not in self.workers:
                self.workers.append(worker)             # !NB
                return f"{worker.name} the {worker.__class__.__name__} hired successfully"
            return "Worker already hired"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        searched_worker = [x for x in self.workers if x.name == worker_name]
        if searched_worker:
            self.workers.remove(searched_worker[0])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_sum = sum([x.salary for x in self.workers])
        if salary_sum <= self.__budget:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_needs = sum([x.money_for_care for x in self.animals])
        if sum_needs <= self.__budget:
            self.__budget -= sum_needs
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        total_animals_count = len(self.animals)
        lions = [x.__repr__() for x in self.animals if x.__class__.__name__ == 'Lion']
        tigers = [x.__repr__() for x in self.animals if x.__class__.__name__ == 'Tiger']
        cheetahs = [x.__repr__() for x in self.animals if x.__class__.__name__ == 'Cheetah']
        NEW_LINE = '\n'
        return f'''You have {total_animals_count} animals
----- {len(lions)} Lions:
{NEW_LINE.join(lions)}
----- {len(tigers)} Tigers:
{NEW_LINE.join(tigers)}
----- {len(cheetahs)} Cheetahs:
{NEW_LINE.join(cheetahs)}'''

    def workers_status(self):
        total_workers_count = len(self.workers)
        keepers = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Keeper']
        caretakers = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Caretaker']
        vets = [x.__repr__() for x in self.workers if x.__class__.__name__ == 'Vet']
        NEW_LINE = '\n'
        return f'''You have {total_workers_count} workers
----- {len(keepers)} Keepers:
{NEW_LINE.join(keepers)}
----- {len(caretakers)} Caretakers:
{NEW_LINE.join(caretakers)}
----- {len(vets)} Vets:
{NEW_LINE.join(vets)}'''
