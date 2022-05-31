from unittest import TestCase, main

from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.table.inside_table import InsideTable

class TeaTest(TestCase):
    def setUp(self) -> None:
        self.t = Tea("Nestea", 2, "Nestle")

    def test_repr(self):
        self.assertEqual(self.t.__repr__(), f" - Nestea Nestle - 2.00ml - 2.50lv")


class TableTest(TestCase):
    def setUp(self) -> None:
        self.i = InsideTable(1, 20)

    def test_reserve(self):
        self.i.reserve(21)
        self.assertEqual(self.i.is_reserved, True)

    def test_get_bill(self):
        self.i.order_drink(Tea('Nestea', 1, 'Nestle'))
        self.i.order_food(Bread('Do', 2))
        self.assertEqual(self.i.get_bill(), 4.50)

if __name__ == '__main__':
    main()
