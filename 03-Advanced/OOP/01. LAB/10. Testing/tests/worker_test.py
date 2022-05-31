from tasks.worker import Worker
from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.w = Worker('Raicho', 5000, 100)

    def test_proper_construction(self):
        self.assertEqual(self.w.name, 'Raicho')
        self.assertEqual(self.w.salary, 5000)
        self.assertEqual(self.w.energy, 100)

    def test_rest_method(self):
        old_energy = self.w.energy
        self.w.rest()
        self.assertEqual(old_energy + 1, self.w.energy)

    def test_work_method_if_energy_not_enough(self):
        data = (0, -32)
        for energy in data:
            self.w.energy = energy
            with self.assertRaises(Exception) as exc:
                self.w.work()
            self.assertEqual(str(exc.exception), 'Not enough energy.')

    def test_work_method_money_incrementation(self):
        old_money = self.w.money
        self.w.work()
        self.assertEqual(old_money + self.w.salary, self.w.money)

    def test_work_method_energy_depletion(self):
        old_energy = self.w.energy
        self.w.work()
        self.assertEqual(old_energy - 1, self.w.energy)

    def test_get_info_method(self):
        self.assertEqual(self.w.get_info(), 'Raicho has saved 0 money.')


if __name__ == '__main__':
    main()
