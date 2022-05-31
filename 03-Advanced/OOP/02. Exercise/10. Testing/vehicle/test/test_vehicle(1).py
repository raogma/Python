from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.v = Vehicle(6.0, 131.0)

    def test_proper_construction(self):
        self.assertEqual(self.v.fuel, 6.0)
        self.assertEqual(self.v.horse_power, 131.0)
        self.assertEqual(self.v.capacity, self.v.fuel)
        self.assertEqual(self.v.fuel_consumption, self.v.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_method_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as exc:
            self.v.drive(200)
        self.assertEqual(str(exc.exception), "Not enough fuel")

    def test_drive_method(self):
        old_fuel = self.v.fuel
        self.v.drive(1)
        self.assertEqual(old_fuel - 1.25, self.v.fuel)

    def test_refuel_if_too_much_fuel(self):
        with self.assertRaises(Exception) as exc:
            self.v.refuel(1)
        self.assertEqual(str(exc.exception), "Too much fuel")

    def test_refuel_method(self):
        self.v.drive(4)
        self.v.refuel(1)
        self.assertEqual(self.v.fuel, 2)

    def test_class_representation(self):
        self.assertEqual(self.v.__str__(), f"The vehicle has 131.0 "
                                           f"horse power with 6.0 fuel left and 1.25 fuel consumption")


if __name__ == '__main__':
    main()
