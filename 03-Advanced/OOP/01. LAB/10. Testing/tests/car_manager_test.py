from tasks.car_manager import Car
from unittest import TestCase, main


class CarTest(TestCase):
    def setUp(self) -> None:
        self.car = Car("a", "b", 1, 4)

    def test_constructor(self):
        self.assertEqual(self.car.make, 'a')
        self.assertEqual(self.car.model, 'b')
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 4)

    def test_set_invalid_make_attr(self):
        with self.assertRaises(Exception) as exc:
            self.car.make = ''
        self.assertEqual(str(exc.exception), 'Make cannot be null or empty!')

    def test_set_invalid_model_attr(self):
        with self.assertRaises(Exception) as exc:
            self.car.model = ''
        self.assertEqual(str(exc.exception), 'Model cannot be null or empty!')

    def test_set_invalid_fuel_consumption_attr(self):
        data = (0, -42)
        for number in data:
            with self.assertRaises(Exception) as exc:
                self.car.fuel_consumption = number
            self.assertEqual(str(exc.exception), 'Fuel consumption cannot be zero or negative!')

    def test_set_invalid_fuel_capacity_attr(self):
        data = (0, -42)
        for number in data:
            with self.assertRaises(Exception) as exc:
                self.car.fuel_capacity = number
            self.assertEqual(str(exc.exception), 'Fuel capacity cannot be zero or negative!')

    def test_set_invalid_fuel_amount_attr(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_amount = -42
        self.assertEqual(str(exc.exception), 'Fuel amount cannot be negative!')

    def test_refuel_with_invalid_fuel(self):
        data = (0, -42)
        for number in data:
            with self.assertRaises(Exception) as exc:
                self.car.refuel(number)
            self.assertEqual(str(exc.exception), 'Fuel amount cannot be zero or negative!')

    def test_refuel_method_with_incorrect_fuel(self):
        data = (0, -42)
        for number in data:
            with self.assertRaises(Exception) as exc:
                self.car.refuel(number)
            self.assertEqual(str(exc.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_method_if_value_above_fuel_capacity(self):
        value = 40
        self.car.refuel(value)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_method_with_value_below_or_equal_to_capacity(self):
        old_fuel_amount = self.car.fuel_amount
        data = (4, 3)
        for value in data:
            self.car.refuel(value)
            self.assertEqual(self.car.fuel_amount, old_fuel_amount + value)
            self.car.fuel_amount = 0

    def test_drive_method_without_enough_fuel(self):
        self.car.refuel(4)
        with self.assertRaises(Exception) as exc:
            self.car.drive(500)
        self.assertEqual(str(exc.exception), "You don't have enough fuel to drive!")

    def test_drive_method(self):
        self.car.refuel(4)
        self.car.drive(400)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == '__main__':
    main()
