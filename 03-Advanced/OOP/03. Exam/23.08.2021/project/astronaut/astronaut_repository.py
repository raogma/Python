class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        a = [x for x in self.astronauts if x.name == name]
        if a:
            return a[0]

    def get_suitable_astronauts(self):
        suitable = {}
        for a in self.astronauts:
            if a.oxygen > 30:
                suitable[a] = a.oxygen

        suitable_up_to_five = []
        suitable = dict(sorted(suitable.items(), key=lambda x: x[1], reverse=True))
        for el in suitable:
            suitable_up_to_five.append(el)
            if len(suitable_up_to_five) == 5:
                break
        return suitable_up_to_five




