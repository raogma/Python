from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.p = PetShop("Tutu")

    def test_init(self):
        self.assertEqual(self.p.name, 'Tutu')
        self.assertEqual(self.p.food, {})
        self.assertEqual(self.p.pets, [])

    def test_add_food_raises_value_error(self):
        for x in (0, -1):
            with self.assertRaises(ValueError) as exc:
                self.p.add_food('Zarno', x)
            self.assertEqual(str(exc.exception), 'Quantity cannot be equal to or less than 0')

    def test_add_food_method(self):
        self.assertEqual(self.p.add_food('Zarno', 1), "Successfully added 1.00 grams of Zarno.")
        self.assertEqual(self.p.food, {'Zarno': 1})

    def test_add_pet_raises_exception(self):
        self.p.add_pet('Zaek')
        with self.assertRaises(Exception) as exc:
            self.p.add_pet('Zaek')
        self.assertEqual(str(exc.exception), 'Cannot add a pet with the same name')

    def test_add_pet_method(self):
        self.assertEqual(self.p.add_pet('Zaek'), "Successfully added Zaek.")
        self.assertEqual(self.p.pets, ['Zaek'])

    def test_feed_pet_invalid_name_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.p.feed_pet('Zarno', 'Zaek')
        self.assertEqual(str(exc.exception), "Please insert a valid pet name")

    def test_feed_pet_food_not_in_place(self):
        self.p.add_pet('Zaek')
        self.assertEqual(self.p.feed_pet('Zarno', 'Zaek'), 'You do not have Zarno')

    def test_feed_pet_less_than_hundred(self):
        self.p.add_food('Zarno', 1)
        self.p.add_pet('Zaek')
        self.assertEqual(self.p.feed_pet('Zarno', 'Zaek'), "Adding food...")
        self.assertEqual(self.p.food['Zarno'], 1001)

    def test_feed_pet_method(self):
        self.p.add_food('Zarno', 200)
        self.p.add_pet('Zaek')
        self.assertEqual(self.p.feed_pet('Zarno', 'Zaek'), "Zaek was successfully fed")
        self.assertEqual(self.p.food['Zarno'], 100)

    def test_repr_method(self):
        self.p.add_pet('Zaek')
        self.p.add_pet('Koche')
        self.assertEqual(self.p.__repr__(), f'''Shop Tutu:
Pets: Zaek, Koche''')



if __name__ == '__main__':
    main()

