class Zoo:
    total_animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fish.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        if species == 'mammal':
            names = ', '.join(self.mammals)
            upper_plural = 'Mammals'
        elif species == 'fish':
            names = ', '.join(self.fish)
            upper_plural = 'Fishes'
        elif species == 'bird':
            names = ', '.join(self.birds)
            upper_plural = 'Birds'
        return f"{upper_plural} in {self.name}: {names}\nTotal animals: {self.total_animals}"



zoo_name = input()
count = int(input())
zoo = Zoo(zoo_name)

for _ in range(count):
    type, animal = input().split()
    zoo.add_animal(type, animal)
    zoo.total_animals += 1

species_to_include = input()
print(zoo.get_info(species_to_include))