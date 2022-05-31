from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.missions = {'Successful': 0, "Unsuccessful": 0}

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == 'Biologist':
            x = Biologist(name)
        elif astronaut_type == 'Geodesist':
            x = Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            x = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")
        o = self.astronaut_repository.find_by_name(name)
        if o is None:
            self.astronaut_repository.add(x)
            return f"Successfully added {astronaut_type}: {name}."
        else:
            return f"{name} is already added."

    def add_planet(self, name: str, items: str):
        x = Planet(name)
        x.add_items(items)
        o = self.planet_repository.find_by_name(name)
        if o:
            return f"{name} is already added."
        self.planet_repository.add(x)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        o = self.astronaut_repository.find_by_name(name)
        if o is None:
            raise Exception(f"Astronaut {name} doesn't exists!")
        self.astronaut_repository.remove(o)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        p = self.planet_repository.find_by_name(planet_name)
        if p is None:
            raise Exception("Invalid planet name!")

        suitable = self.astronaut_repository.get_suitable_astronauts()
        if not suitable:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_in_open = 0
        for a in suitable:
            astronauts_in_open += 1
            while a.oxygen > 0:
                if p.items:
                    item = p.items.pop()
                    a.breathe()
                    a.backpack.append(item)
                else:
                    self.missions['Successful'] += 1
                    return f"Planet: {planet_name} was explored. {astronauts_in_open} astronauts participated in collecting items."
        self.missions['Unsuccessful'] += 1
        return "Mission is not completed."

    def report(self):
        res = f'''{self.missions['Successful']} successful missions!
{self.missions['Unsuccessful']} missions were not completed!
Astronauts' info:\n'''
        for a in self.astronaut_repository.astronauts:
            res += f'''Name: {a.name}
Oxygen: {a.oxygen}
Backpack items: {"none" if not a.backpack else ", ".join(a.backpack)}\n'''
        return res
