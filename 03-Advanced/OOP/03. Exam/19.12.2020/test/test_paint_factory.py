from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):
    def setUp(self) -> None:
        self.f = PaintFactory('emag', 10)

    def test_init(self):
        self.assertEqual(self.f.name, 'emag')
        self.assertEqual(self.f.capacity, 10)

    def test_add_ingredient_invalid_ingredient(self):
        with self.assertRaises(TypeError) as exc:
            self.f.add_ingredient('butter', 10)
        self.assertEqual(str(exc.exception), f"Ingredient of type butter not allowed in PaintFactory")

    def test_add_ingredient_invalid_quantity(self):
        with self.assertRaises(ValueError) as exc:
            self.f.add_ingredient('white', 11)
        self.assertEqual(str(exc.exception), "Not enough space in factory")

    def test_add_ingredient(self):
        self.f.add_ingredient('white', 10)
        self.assertEqual(self.f.ingredients, {'white': 10})

    def test_remove_ingredient_invalid_ingredient_name(self):
        with self.assertRaises(KeyError) as exc:
            self.f.remove_ingredient('white', 10)       # !!!
        self.assertEqual(str(exc.exception), "'No such ingredient in the factory'")

    def test_remove_ingredient_invalid_ingredient_quantity(self):
        self.f.add_ingredient('white', 10)
        with self.assertRaises(ValueError) as exc:
            self.f.remove_ingredient('white', 15)
        self.assertEqual(str(exc.exception), "Ingredients quantity cannot be less than zero")

    def test_remove_ingredient(self):
        self.f.add_ingredient('white', 10)
        self.f.remove_ingredient('white', 5)
        self.assertEqual(self.f.ingredients['white'], 5)

    def test_products_property(self):
        self.f.add_ingredient('white', 10)
        self.assertEqual(self.f.products, {'white': 10})

    def test_can_add(self):
        self.f.add_ingredient('white', 10)
        self.assertEqual(self.f.can_add(1), False)



if __name__ == '__main__':
    main()