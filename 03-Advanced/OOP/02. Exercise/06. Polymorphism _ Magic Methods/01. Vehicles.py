from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    @abstractmethod
    def drive(self, distance):
        required_fuel = distance * (self.fuel_consumption + self.AIR_CONDITIONING)
        if self.fuel_quantity - required_fuel >= 0:
            self.fuel_quantity -= required_fuel

    @abstractmethod
    def refuel(self, fuel):
        self.fuel_quantity += fuel

    @property
    def AIR_CONDITIONING(self):
        return self.AIR_CONDITIONING


class Truck(Vehicle, ABC):
    AIR_CONDITIONING = 1.6

    def drive(self, distance):
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel * 0.95)


class Car(Vehicle, ABC):
    AIR_CONDITIONING = 0.9

    def drive(self, distance):
        super().drive(distance)

    def refuel(self, fuel):
        super().refuel(fuel)


# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
