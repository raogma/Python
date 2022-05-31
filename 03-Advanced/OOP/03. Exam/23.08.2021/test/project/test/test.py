from project.library import Library
from unittest import TestCase, main


class LibraryTest(TestCase):
    def setUp(self) -> None:
        self.l = Library('Test')

    def test_constructor(self):
        self.assertEqual(self.l.name, 'Test')
        self.assertEqual(self.l.books_by_authors, {})
        self.assertEqual(self.l.readers, {})

    def test_name_empty_string(self):
        with self.assertRaises(ValueError) as exc:
            self.l.name = ''
        self.assertEqual(str(exc.exception), "Name cannot be empty string!")

    def test_add_book_author_not_in_authors(self):
        self.l.add_book('Pesho', 'Gora')
        self.assertEqual(self.l.books_by_authors, {'Pesho': ['Gora']})

    def test_add_book_author_in_authors(self):
        self.l.add_book('Pesho', 'Gora')
        self.l.add_book('Pesho', 'More')
        self.assertEqual(self.l.books_by_authors, {'Pesho': ['Gora', 'More']})

    def test_add_book_title_exists(self):
        self.l.add_book('Pesho', 'Gora')
        self.l.add_book('Pesho', 'Gora')
        self.assertEqual(self.l.books_by_authors, {'Pesho': ['Gora']})

    def test_add_reader(self):
        self.l.add_reader('Gosho')
        self.assertEqual(self.l.readers, {'Gosho': []})

    def test_add_reader_exists(self):
        self.l.add_reader('Gosho')
        self.assertEqual(self.l.add_reader('Gosho'), "Gosho is already registered in the Test library.")

    def test_rent_book_reader_not_exists(self):
        self.assertEqual(self.l.rent_book('Gosho', 'Pesho', 'Gora'), "Gosho is not registered in the Test Library.")

    def test_rent_book_author_not_exists(self):
        self.l.add_reader('Gosho')
        self.assertEqual(self.l.rent_book('Gosho', 'Pesho', 'Gora'), "Test Library does not have any Pesho's books.")

    def test_rent_book_book_not_exists(self):
        self.l.add_reader('Gosho')
        self.l.add_book('Pesho', 'Gora')
        self.assertEqual(self.l.rent_book('Gosho', 'Pesho', 'More'), """Test Library does not have Pesho's "More".""")

    def test_rent_book_readers_dict(self):
        self.l.add_reader('Gosho')
        self.l.add_book('Pesho', 'Gora')
        self.l.rent_book('Gosho', 'Pesho', 'Gora')
        self.assertEqual(self.l.readers, {'Gosho': [{'Pesho': 'Gora'}]})
        self.assertEqual(self.l.books_by_authors, {'Pesho': []})

if __name__ == '__main__':
    main()

