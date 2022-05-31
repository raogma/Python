from unittest import TestCase, main
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.space_station import SpaceStation


class TestAstronautRepo(TestCase):
    def setUp(self) -> None:
        self.repo = AstronautRepository()
        self.station = SpaceStation()
        self.b1 = Biologist('Gosho')
        self.b2 = Biologist('Pesho')
        self.m1 = Meteorologist('Ivan')
        self.m2 = Meteorologist('Mitko')
        self.g1 = Geodesist('Pepi')
        self.g2 = Geodesist('Unknown')
        self.g2.oxygen = 5
        self.repo.add(self.b1)
        self.repo.add(self.b2)
        self.repo.add(self.m1)
        self.repo.add(self.m2)
        self.repo.add(self.g1)
        self.repo.add(self.g2)
        self.p = Planet('Gora')
        self.p.add_items('Gabi, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba, Chorba')
        self.planet_repo = PlanetRepository()
        self.planet_repo.add(self.p)
        self.station.planet_repository.add(self.p)
        # self.station.astronaut_repository.add(self.b1)
        # self.station.astronaut_repository.add(self.b2)
        self.station.astronaut_repository.add(self.m1)
        # self.station.astronaut_repository.add(self.m2)
        # self.station.astronaut_repository.add(self.g1)
        # self.station.astronaut_repository.add(self.g2)

    def test_constructor(self):
        self.assertEqual(self.repo.astronauts, [self.b1, self.b2, self.m1, self.m2, self.g1, self.g2])

    def test_get_suitable_if_5(self):
        self.assertEqual(self.repo.get_suitable_astronauts(), [self.m1, self.m2, self.b1, self.b2, self.g1])

    def test_suitable_empty(self):
        self.assertEqual(AstronautRepository().get_suitable_astronauts(), [])

    def test_pRepo(self):
        self.assertEqual(self.planet_repo.planets, [self.p])

    def test_mission_(self):
        self.station.send_on_mission('Gora')
        self.assertEqual(self.station.report(), '')


if __name__ == '__main__':
    main()