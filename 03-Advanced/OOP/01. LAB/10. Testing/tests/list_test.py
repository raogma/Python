from tasks.list import IntegerList
from unittest import TestCase, main


class IntegerListTest(TestCase):
    def setUp(self) -> None:
        self.inl = IntegerList([])

    def test_get_data_method(self):
        self.assertEqual(self.inl.get_data(), [])

    def test_add_method(self):
        self.assertEqual(self.inl.add(8), [8])

    def test_add_with_incorrect_type(self):
        with self.assertRaises(ValueError) as exc:
            self.inl.add('dqdo')
        self.assertEqual(str(exc.exception), 'Element is not Integer')

    def test_remove_method(self):
        self.inl.add(8)
        self.assertEqual(self.inl.remove_index(0), 8)
        self.assertEqual(self.inl.get_data(), [])

    def test_remove_with_incorrect_index(self):
        with self.assertRaises(IndexError) as exc:
            self.inl.remove_index(0)
        self.assertEqual(str(exc.exception), 'Index is out of range')

    def test_get_method(self):
        self.inl.add(8)
        self.assertEqual(self.inl.get(0), 8)

    def test_get_method_with_incorrect_index(self):
        with self.assertRaises(IndexError) as exc:
            self.inl.get(0)
        self.assertEqual(str(exc.exception), 'Index is out of range')

    def test_insert_method(self):
        self.inl.add(8)
        self.inl.insert(0, 7)
        self.assertEqual(self.inl.get_data(), [7, 8])

    def test_insert_with_incorrect_index(self):
        with self.assertRaises(IndexError) as exc:
            self.inl.insert(0, 8)
        self.assertEqual(str(exc.exception), 'Index is out of range')

    def test_insert_with_incorrect_type(self):
        self.inl.add(8)
        with self.assertRaises(ValueError) as exc:
            self.inl.insert(0, 'dqdo')
        self.assertEqual(str(exc.exception), 'Element is not Integer')

    def test_get_biggest_method(self):
        self.inl.add(7)
        self.inl.add(8)
        self.assertEqual(self.inl.get_biggest(), 8)

    def test_get_index_method(self):
        self.inl.add(8)
        self.assertEqual(self.inl.get_index(8), 0)


if __name__ == '__main__':
    main()