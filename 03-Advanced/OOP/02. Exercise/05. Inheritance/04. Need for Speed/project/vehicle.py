class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self,
                 fuel: float,
                 horse_power: int):
        self.horse_power = horse_power
        self.fuel = fuel
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel -= self.fuel_consumption * kilometers

