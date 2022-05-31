from tasks.cat import Cat
import unittest


class CatTest(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Cat('Joe')

    def test_initialization(self):
        self.assertEqual(self.c.name, 'Joe')

    def test_eat_method_if_already_fed(self):
        self.c.fed = True
        with self.assertRaises(Exception) as exc:
            self.c.eat()
        self.assertEqual(str(exc.exception), 'Already fed.')

    def test_eat_method(self):
        self.c.fed = False
        old_size = self.c.size
        self.c.eat()
        self.assertTrue(self.c.fed)
        self.assertTrue(self.c.sleepy)
        self.assertEqual(self.c.size, old_size + 1)

    def test_sleep_method_if_hungry(self):
        self.c.fed = False
        with self.assertRaises(Exception) as exc:
            self.c.sleep()
        self.assertEqual(str(exc.exception), 'Cannot sleep while hungry')

    def test_sleep_method(self):
        self.c.eat()
        self.c.sleep()
        self.assertFalse(self.c.sleepy)


if __name__ == '__main__':
    unittest.main()
