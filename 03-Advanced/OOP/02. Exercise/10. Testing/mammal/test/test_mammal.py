from project.mammal import Mammal
import unittest


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Mammal('Joe', 'dog', 'woof')

    def test_proper_construction(self):
        self.assertEqual(self.m.name, 'Joe')
        self.assertEqual(self.m.type, 'dog')
        self.assertEqual(self.m.sound, 'woof')
        self.assertEqual(self.m._Mammal__kingdom, 'animals')

    def test_make_sound_method(self):
        self.assertEqual(self.m.make_sound(), f"Joe makes woof")

    def test_get_kingdom_method(self):
        self.assertEqual(self.m.get_kingdom(), "animals")

    def test_info_method(self):
        self.assertEqual(self.m.info(), f"Joe is of type dog")


if __name__ == '__main__':
    unittest.main()