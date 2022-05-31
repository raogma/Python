from unittest import TestCase, main

from project.hardware.hardware import Hardware
from project.software.light_software import LightSoftware


class HardwareTest(TestCase):
    def setUp(self) -> None:
        self.h = Hardware('HDD', 'Heavy', 200, 200)
        self.s = LightSoftware('Test', 1000, 100)
        self.s2 = LightSoftware('Test2', 100, 1000)
        self.s3 = LightSoftware('Test3', 100, 100)
        self.s4 = LightSoftware('Test4', 20, 20)

    def test_init(self):
        self.assertEqual(self.h.name, 'HDD')
        self.assertEqual(self.h.type, 'Heavy')
        self.assertEqual(self.h.capacity, 200)
        self.assertEqual(self.h.memory, 200)
        self.assertEqual(self.h.software_components, [])

    def test_install_raises_exception_capacity_consumption(self):
        with self.assertRaises(Exception) as exc:
            self.h.install(self.s)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_install_raises_exception_memory_consumption(self):
        with self.assertRaises(Exception) as exc:
            self.h.install(self.s2)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_install(self):
        self.h.install(self.s3)
        self.assertEqual(len(self.h.software_components), 1)

    def test_uninstall(self):
        self.h.install(self.s3)
        self.h.uninstall(self.s3)
        self.assertEqual(self.h.software_components, [])

    def test_not_existing_uninstall(self):
        self.h.install(self.s4)
        self.h.uninstall(self.s3)
        self.assertEqual(self.h.software_components, [self.s4])


if __name__ == '__main__':
    main()