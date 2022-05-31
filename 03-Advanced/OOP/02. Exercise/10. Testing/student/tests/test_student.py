from project.student import Student
from unittest import TestCase, main


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.s = Student('Raicho')

    def test_proper_construction(self):
        self.assertEqual(self.s.name, 'Raicho')
        self.assertEqual(self.s.courses, {})

    def test_enroll_method_same_course(self):
        self.s.courses['softuni'] = ['a', 'b']
        self.assertEqual(self.s.enroll('softuni', ['c', 'd'], 'dqdo'), "Course already added. "
                                                                       "Notes have been updated.")
        self.assertEqual(self.s.courses, {'softuni': ['a', 'b', 'c', 'd']})

    def test_enroll_method_add_course_notes_Y(self):
        self.assertEqual(self.s.enroll('softuni', ['c', 'd'], 'Y'),  "Course and course notes have been added.")
        self.assertEqual(self.s.courses, {'softuni': ['c', 'd']})

    def test_enroll_method_add_course_notes_emptystr(self):
        self.assertEqual(self.s.enroll('softuni', ['c', 'd'], ''), "Course and course notes have been added.")
        self.assertEqual(self.s.courses, {'softuni': ['c', 'd']})

    def test_enroll_method(self):
        self.assertEqual(self.s.enroll('softuni', ['c', 'd'], 'dqdo'), "Course has been added.")
        self.assertEqual(self.s.courses, {'softuni': []})

    def test_add_notes_method_course_not_found(self):
        with self.assertRaises(Exception) as exc:
            self.s.add_notes('softuni', ['a'])
        self.assertEqual(str(exc.exception), "Cannot add notes. Course not found.")

    def test_add_notes_method(self):
        self.s.courses['softuni'] = ['a', 'b']
        self.assertEqual(self.s.add_notes('softuni', 'c'), "Notes have been updated")
        self.assertEqual(self.s.courses, {'softuni': ['a', 'b', 'c']})

    def test_leave_course_method_not_found(self):
        with self.assertRaises(Exception) as exc:
            self.s.leave_course('softuni')
        self.assertEqual(str(exc.exception), "Cannot remove course. Course not found.")

    def test_leave_course_method(self):
        self.s.courses = {'softuni': []}
        self.assertEqual(self.s.leave_course('softuni'), "Course has been removed")


if __name__ == '__main__':
    main()
