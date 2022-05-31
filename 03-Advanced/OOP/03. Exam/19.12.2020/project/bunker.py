class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        l = [x for x in self.supplies if x.__class__.__name__ == 'FoodSupply']
        if not l:
            raise IndexError("There are no food supplies left!")
        return l

    @property
    def water(self):
        l = [x for x in self.supplies if x.__class__.__name__ == 'WaterSupply']
        if not l:
            raise IndexError("There are no water supplies left!")
        return l

    @property
    def painkillers(self):
        l = [x for x in self.medicine if x.__class__.__name__ == 'Painkiller']
        if not l:
            raise IndexError("There are no painkillers left!")
        return l

    @property
    def salves(self):
        l = [x for x in self.supplies if x.__class__.__name__ == 'Salve']
        if not l:
            raise IndexError("There are no salves left!")
        return l

    def add_survivor(self, survivor: object):
        if survivor in self.survivors:
            raise ValueError("Survivor with name {name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: object):
        self.supplies.append(supply)

    def add_medicine(self, medicine: object):
        self.medicine.append(medicine)

    def heal(self, survivor: object, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == 'Painkiller':
                o = self.painkillers.pop()
            elif medicine_type == 'Salve':
                o = self.salves.pop()
            else:
                return 'Wrong medicine type!'

            self.medicine.remove(o)
            o.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: object, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == 'FoodSupply':
                o = self.food.pop()
            elif sustenance_type == 'WaterSupply':
                o = self.water.pop()
            else:
                return 'Wrong supply type!'

            self.supplies.remove(o)
            o.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for s in self.survivors:
            s.needs -= s.age * 2
            self.sustain(s, 'FoodSupply')
            self.sustain(s, 'WaterSupply')

